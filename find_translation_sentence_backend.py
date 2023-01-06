import json
import get_translation_function as g

import flask
from flask import Flask, request
from flask_cors import CORS

#initialize Flask object and enable CORS on all routes
app = Flask(__name__)
CORS(app)

@app.route('/words', methods=["POST"])
def words():
    print("words endpoint reached...")

    if request.method == "POST":
        received_data = request.get_json()
        message = received_data['data']
        return_data = json.dumps(g.findtranslations(message))
        #print(g.findtranslations(message))
        return flask.Response(response=return_data, status=201)

#only run the Flask application if this file is executed as a script and not imported
if __name__ == "__main__":
    app.run("localhost", 6969)
