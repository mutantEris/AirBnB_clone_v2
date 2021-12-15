#!/usr/bin/python3
"""Flask Scripts"""
from flask import Flask
from flask import render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    return "Hello HBNB!"


@app.route('/hbnb')
def hey():
    return "HBNB"


@app.route('/c/<text>')
def yo(text):
    return "C {}".format(text.replace("_", " "))


@app.route('/python/')
@app.route('/python/<text>')
def sup(text="is cool"):
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>')
def howdy(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def whyareyouinmyhouse(n=None):
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
