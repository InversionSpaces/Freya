import os
from flask import Flask

app = Flask(__name__, static_url_path="/static")

import freya.views
import freya.service

if __name__ == "__main__":
    app.run(debug=True)

