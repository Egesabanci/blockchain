import os
from flask_sqlalchemy import SQLAlchemy

from .app import app
from .app import cfg 

# create database folder in current path
DB_PATH = os.path.join(os.getcwd(), "src")
if "database" not in os.listdir(DB_PATH):
	os.mkdir(os.path.join(DB_PATH, "database"))

# database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/" + cfg["db_name"]
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = cfg["track_modifications"]

# main database instance
db = SQLAlchemy(app)

# all models from models.py
from .models import *

# create database if not exists in "current_path/database"
if os.listdir(os.path.join(DB_PATH, "database")) == []:
	db.create_all()