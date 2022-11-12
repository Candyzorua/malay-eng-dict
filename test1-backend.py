import json

import flask
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/words', methods=["GET"])
def users():
    print("words endpoint reached...")
    with open("malay-eng-dict.json", "r") as f:
        data = json.load(f)
        return flask.jsonify(data)

if __name__ == "__main__":
    app.run("localhost", 6969)