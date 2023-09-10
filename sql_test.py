import hh_api
import sqlite3

# text = "Python"
#
# conn = sqlite3.connect('hh.sqlite')
#
# cur = conn.cursor()
#
# requirements = hh_api.func_parser(text)
#
# cur.execute("SELECT * FROM input_text WHERE input_text=?", (text,))
# answer = cur.fetchone()
#
# if answer is None:
#     cur.execute("INSERT INTO input_text VALUES(null, ?)", (text,))
#
# cur.execute("SELECT * FROM input_text WHERE input_text=?", (text,))
# answer = cur.fetchone()
# input_id = answer[0]
#
# for req in requirements:
#     cur.execute("SELECT * FROM key_skills WHERE key_skills=?", (req["name"],))
#     answer = cur.fetchone()
#
#     if answer is None:
#         cur.execute("INSERT INTO key_skills VALUES(null, ?)", (req["name"],))
#
#     cur.execute("SELECT * FROM key_skills WHERE key_skills=?", (req["name"],))
#     answer = cur.fetchone()
#     skill_id = answer[0]
#
#     cur.execute("SELECT * FROM input_text_key_skills WHERE input_text_key_skills.id_input_text = ? AND input_text_key_skills.id_key_skills = ?", (input_id, skill_id))
#     res = cur.fetchone()
#     if res:
#         cur.execute("UPDATE input_text_key_skills SET count = ?, percent = ? WHERE input_text_key_skills.id_input_text = ? AND input_text_key_skills.id_key_skills = ?", (req["count"], req["percent"], input_id, skill_id))
#     else:
#         cur.execute("INSERT INTO input_text_key_skills VALUES(null, ?, ?, ?, ?)", (input_id, skill_id, req["count"], req["percent"]))
#
# conn.commit()
# conn.close()


# if __name__ == "__main__":
#     requirements = [{"name": "Python", "count": 92, "percent": 14.51}, {"name": "Git", "count": 40, "percent": 6.31},
#                       {"name": "PostgreSQL", "count": 40, "percent": 6.31},
#                       {"name": "Linux", "count": 32, "percent": 5.05}, {"name": "SQL", "count": 24, "percent": 3.79},
#                       {"name": "Django Framework", "count": 23, "percent": 3.63},
#                       {"name": "Docker", "count": 21, "percent": 3.31},
#                       {"name": "\u041e\u041e\u041f", "count": 13, "percent": 2.05},
#                       {"name": "Redis", "count": 11, "percent": 1.74}, {"name": "MySQL", "count": 10, "percent": 1.58},
#                       {"name": "Django", "count": 10, "percent": 1.58},
#                       {"name": "RabbitMQ", "count": 8, "percent": 1.26},
#                       {"name": "FastAPI", "count": 8, "percent": 1.26}, {"name": "Flask", "count": 7, "percent": 1.1},
#                       {"name": "REST", "count": 6, "percent": 0.95}, {"name": "API", "count": 6, "percent": 0.95},
#                       ]

