import json

import flask
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def findtranslation (malayword):
    with open("malay-eng-dict.json", "r") as f:
        if malayword not in f:
            return ("Sorry, word not found.")
        else:
            engword = f[malayword]
            return f"English translation(s): {engword}"

@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/words', methods=["GET", "POST"])
def words():
    print("words endpoint reached...")

    if request.method == "GET":
        with open("malay-eng-dict.json", "r") as f:
            data = json.load(f)
            return flask.jsonify(data)

    if request.method == "POST":
        received_data = request.get_json()
        print(f"received data: {received_data}")
        message = received_data['data']
        return_data = findtranslation(message)
        return flask.Response(response=return_data, status=201)

if __name__ == "__main__":
    app.run("localhost", 6969)