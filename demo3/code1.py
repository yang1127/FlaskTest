# -*-coding:utf-8-*-
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/home")
def demo1():
    return render_template("home.html")


if __name__ == '__main__':
    app.run()