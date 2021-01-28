from flask import Flask

# main app instance
app = Flask(__name__)

# all routes from routes.py
from .routes import *