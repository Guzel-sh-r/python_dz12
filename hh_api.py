import requests
import pprint
import json


def func_converter_curr(curr, amount):
    text = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').text # запрос данных по валютам
    all_value = json.loads(text)
    try:
        payment = all_value["Valute"][curr]["Value"] / all_value["Valute"][curr]["Nominal"] * float(amount)
    except KeyError:
        payment = amount

    return int(payment)


def func_hh(num, text):
    url = 'https://api.hh.ru/vacancies'
    params = {
        'text': text,
        'page': num,
    }
    result = requests.get(url, params=params).json()
    items = result["items"]
    return items


def func_parser(text):
    url = 'https://api.hh.ru/vacancies'
    result = requests.get(url, params={'text': text, 'page': 0}).json()
    # pprint.pprint(result)
    items = result["items"]
    pages = result["pages"]
    per_page = result["per_page"]
    found = result["found"]

    answer_count = 0
    if pages >= 5:
        pages = 5

    result = {'keywords': text,
              'count': answer_count,
              'salary_average': 0,
              'requirements': []
              }

    all_snippet, all_salary = {}, []
    # pprint.pprint(items)


    for p in range(pages):
        items = func_hh(p, text)
        # print(f"Страница №{p}")
        for i in range(len(items)):
            snippet = set()
            url_vacancy = items[i]["url"]
            result_vacancy = requests.get(url_vacancy).json()
            # pprint.pprint(result_vacancy)

            key_skills = result_vacancy["key_skills"]

            if len(key_skills) > 0:
                for key_skill in key_skills:
                    snippet.add(key_skill["name"])
                for val in snippet:
                    if val[-1] == "-":
                        val0 = val[:-1]
                    else:
                        val0 = val
                    if val0 in all_snippet:
                        all_snippet[val0] += 1
                    else:
                        all_snippet[val0] = 1

                salary = result_vacancy["salary"]
                if salary is not None:
                    curr = salary["currency"]
                    salary_from = salary["from"]
                    salary_to = salary["to"]
                    if salary_from is None and salary_to is None:
                        salary = 0
                    elif salary_to is None and salary_from is not None:
                        salary = salary_from
                    elif salary_from is None and salary_to is not None:
                        salary = salary_to
                    else:
                        salary = (int(salary_from) + int(salary_to) / 2)

                    if curr != "RUR":
                        salary = func_converter_curr(curr, salary)
                else:
                    salary = 0

                all_salary.append(salary)

                answer_count += 1

    try:
        result["salary_average"] = int(sum(all_salary) / len(all_salary))

        all_count = 0
        for i in all_snippet:
            all_count += int(all_snippet[i])

        add, add_sort = [], []
        for name, count in all_snippet.items():
            add.append({"name": name,
                        "count": count,
                        "percent": round((count / all_count) * 100, 2)})

        [add_sort.append(i) for i in sorted(add, key=lambda x: x['count'], reverse=True)]

        result["requirements"] = add_sort

        result["count"] = answer_count

        with open("result.json", mode="w") as f:
            json.dump(result, f)

    except ZeroDivisionError:
        result["salary_average"] = 0
        result["requirements"] = ""
        result["count"] = 0

    with open("result.json", mode="w") as f:
        json.dump(result, f)


    return result["requirements"][:3]
