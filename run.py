from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route("/ol/ol.js")
def ol():
    with open("ol/ol.js") as f:
        return f.read()

@app.route("/")
def index():
    return render_template("map.html")

@app.route("/data")
def data():
    with open("geoex.json") as f:
        return jsonify(json.load(f))

app.run()
