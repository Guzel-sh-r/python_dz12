import requests
import pprint
import json
import re


url = 'https://api.hh.ru/vacancies'

def func_converter_curr(curr, amount):
    text = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').text # запрос данных по валютам
    all_value = json.loads(text)
    try:
        payment = float(amount) * all_value["Valute"][curr]["Value"]
    except KeyError:
        payment = amount

    return int(payment)


def func_hh(num, text):
    params = {
        'text': text,
        'page': num,
    }
    result = requests.get(url, params=params).json()
    items = result["items"]
    return items

text = input("Введите интересующую вакансию: ")

result = requests.get(url, params={'text': text, 'page': 0}).json()

items = result["items"]
pages = result["pages"]
per_page = result["per_page"]
found = result["found"]

all_quantity = pages * per_page
if found >= all_quantity:
    answer_count = all_quantity
else:
    answer_count = per_page

result = {'keywords': text,
          'count': answer_count,
          'salary_average': 0,
          'requirements': []
          }

all_snippet, all_salary = {}, []
# pprint.pprint(items)

for p in range(pages):
    items = func_hh(p, text)
    print(f"Страница №{p}")
    for i in range(len(items)):
        snippet = set()
        val1 = items[i]["snippet"]["requirement"]
        val2 = items[i]["snippet"]["responsibility"]
        if val1 is not None:
            val1 = val1.replace("<highlighttext>Python</highlighttext>", "Python")
            snippet1 = re.findall(r'\s[A-Za-z-?]+', val1)
            snippet11 = [j.lower().strip() for j in snippet1]
            snippet.update(snippet11)

        if val2 is not None:
            snippet2 = re.findall(r'\s[A-Za-z-?]+', val2)
            snippet22 = [j.lower().strip() for j in snippet2]
            snippet.update(snippet22)

        snippet.discard("-")

        for val in snippet:
            if val[-1] == "-":
                val0 = val[:-1]
            else:
                val0 = val
            if val0 in all_snippet:
                all_snippet[val0] += 1
            else:
                all_snippet[val0] = 1

        salary = items[i]["salary"]
        if salary is not None:
            curr = salary["currency"]
            if salary["from"] is None:
                salary = salary["to"]
            elif salary["to"] is None:
                salary = salary["from"]
            else:
                salary = int((salary["to"] + salary["from"]) / 2)
        else:
            salary = 0
            curr = "RUR"

        if curr != "RUR":
            salary = func_converter_curr(curr, salary)

        all_salary.append(salary)

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

with open("result.json", mode="w") as f:
    json.dump(result, f)
