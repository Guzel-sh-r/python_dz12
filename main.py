from flask import Flask, render_template, request
import hh_api

app = Flask(__name__)

@app.get("/index/")
@app.get("/")
def index():
    return render_template("index.html")


@app.route("/contact/")
def contact():
    contact = "телеграм https://t.me/guzelshr"
    return render_template("contact.html", contacts=contact)

@app.route("/form/")
def form():
    return render_template("form.html")

@app.post("/results/")
def results():
    text = request.form
    requirements = hh_api.func_parser(text["query_string"])
    data = hh_api.func_sql(text["query_string"], requirements[:5])
    return render_template("results.html", key=text["query_string"], data=requirements[:5])


if __name__ == "__main__":
    app.run(debug=True)
