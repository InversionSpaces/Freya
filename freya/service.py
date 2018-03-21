import os

from flask import jsonify
from flask import json

from freya import app

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

@app.route("/data")
def data():
    with open(os.path.join(__location__, "../data/geoex.json")) as f:
        return jsonify(json.load(f))
