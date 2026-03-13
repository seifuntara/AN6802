from flask import Flask, render_template, request
import joblib
import os
from groq import Groq



app = Flask(__name__)

client = Groq()


@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    return(render_template("main.html"))

@app.route("/ethics",methods=["GET","POST"])
def ethics():
    return(render_template("ethics.html"))

@app.route("/correct",methods=["GET","POST"])
def correct():
    return(render_template("correct.html"))

@app.route("/wrong",methods=["GET","POST"])
def wrong():
    return(render_template("wrong.html"))

@app.route("/econ",methods=["GET","POST"])
def econ():
    return(render_template("econ.html"))

@app.route("/foodexp",methods=["GET","POST"])
def foodexp():
    salary = float(request.form.get("salary"))
    model = joblib.load('foodexp.pkl')
    r = model.predict([[salary]])
    return(render_template("foodexp.html",r=r))

@app.route("/chatbot", methods=["GET","POST"])
def chatbot():
    r = None
    query = request.form.get("query")

    if query:
        completion = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "user",
                    "content": query
                }
            ]
        )
        r = completion.choices[0].message.content

    return render_template("chatbot.html", r=r)

if __name__ == "__main__":
    app.run()