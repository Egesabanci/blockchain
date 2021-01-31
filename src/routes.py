from flask import request, render_template
from flask import jsonify

from .app import app
from .database import db
from .models import Blockchain

# index route - serving main.html, get chain info
@app.route("/", methods = ["GET"])
def index():
	if request.method == "GET":
		# get all info from database
		query = Blockchain.query.all()

		# parse all info
		info = {
			"num_of_blocks": len(query),
			"final_block_hash": query[-1].block_hash,
			"last_block_date": query[-1].block_date,
			"genesis_block_hash": query[0].block_hash  
		}

		return render_template("main.html", context = info)

	else:
		return jsonify({"message" : "request is not valid"})
		
# add route - adding new blocks to the chain
@app.route("/add", methods = ["POST"])
def add_block():
	pass