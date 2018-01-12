from flask import render_template
from freya import app

@app.route("/", methods=['GET'])
def index():
    return render_template("map.html")
