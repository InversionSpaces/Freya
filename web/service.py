import json

from flask import jsonify

from web import app

@app.route("/data/data", methods=['GET'])
def data():
    with open("data/geoex.json") as f:
        return jsonify(json.load(f))

@app.route("/ol/ol.js", methods=['GET'])
def ol():
    with open("ol/ol.js") as f:
        return f.read()
        
@app.route("/script/map.js", methods=['GET'])
def map():
    with open("script/map.js") as f:
        return f.read()
        
@app.route("/script/checker.js", methods=['GET'])
def checker():
    with open("script/checker.js") as f:
        return f.read()
        
@app.route("/script/styles.js", methods=['GET'])
def styles():
    with open("script/styles.js") as f:
        return f.read()
