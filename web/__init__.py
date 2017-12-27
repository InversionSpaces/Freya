from flask import Flask

app = Flask(__name__)

import web.views
import web.service

