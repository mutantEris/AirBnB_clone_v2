#!/usr/bin/python3
"""These are scripts for Flask applications"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """This one says Hello HBNB!"""
    return "Hello HBNB!"


if __name__ = "__main__":
    app.run(host="0.0.0.0", port="5000")
