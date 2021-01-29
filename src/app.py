from flask import Flask

# main app instance
app = Flask(__name__)

# read app configurations
with open(os.path.join(os.getcwd(), "src", "config.yml"), "r") as config:
	cfg = yaml.safe_load(config)["config"]

# all routes from routes.py
from .routes import *