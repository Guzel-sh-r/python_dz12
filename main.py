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
    data = hh_api.func_parser(text["query_string"])
    print(data)
    return render_template("results.html", key=text["query_string"], data=data)


if __name__ == "__main__":
    app.run(debug=True)
