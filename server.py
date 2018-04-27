#!/usr/bin/env python

from flask import Flask, request, abort

app = Flask(__name__)

userfunc = None


@app.route('/', methods=['GET', 'POST', 'PUT', 'HEAD', 'OPTIONS', 'DELETE'])
def f():
    if request.data:
        name = request.get_json()["name"]
    else:
        name = "World"
    return "Hello, " + name + " from Python!\n"


app.run(host='0.0.0.0', port=8000)
