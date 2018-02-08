from flask import request, jsonify
from flaskapp import app
import json

@app.route("/", methods=['GET'])
def index():
    message = {}
    message['model'] = 'hello from the ansible flask'
    return jsonify(message)
