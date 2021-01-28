import os
import yaml
from flask_sqlalchemy import SQLAlchemy

from app import app

# configurations
with open("config.yml", "r") as configurations:
	cfg = yaml.safe_load(configurations)["config"]

# database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:////{cfg["db_name"]}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] cfg["track_modifications"]

# main database instance
db = SQLAlchemy(app)

# create database if not exists
if cfg["db_name"] not in os.listdir(os.getcwd()):
	db.create_all()

# all models of the database
