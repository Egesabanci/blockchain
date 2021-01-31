import os
from flask_sqlalchemy import SQLAlchemy

from .app import app
from .app import cfg

# create database folder in current path
DB_PATH = os.path.join(os.getcwd(), "src")
if "database_src" not in os.listdir(DB_PATH):
	os.mkdir(os.path.join(DB_PATH, "database_src"))

# database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database_src/" + cfg["db_name"]
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = cfg["track_modifications"]

# main database instance
db = SQLAlchemy(app)

from .models import Chain
from .blockchain import Blockchain 

# all models from models.py
from .models import *

# create database if not exists in "current_path/database"
if os.listdir(os.path.join(DB_PATH, "database_src")) == []:
	db.create_all()

# if there is no blocks - create genesis block
if len(Chain.query.all()) == 0:
	blockchain = Blockchain(database_instance = Chain)
	genesis_block = blockchain.genesis()

	# add genesis block to the database
	genesis_block = Chain(block_id = genesis_block.block_id,
		block_hash = genesis_block.block_hash,
		block_data = genesis_block.block_data,
		block_date = genesis_block.block_date)

	db.session.add(genesis_block)
	db.session.commit()