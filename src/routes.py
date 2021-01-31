from flask import request, render_template
from flask import jsonify, redirect, url_for

from .app import app
from .database import db
from .models import Chain
from .blockchain import Blockchain

# index route - serving main.html, get chain info
@app.route("/", methods = ["GET"])
def index():
	if request.method == "GET":
		# get all info from database
		query = Chain.query.all()

		# parse all info
		info = {
			"num_of_blocks": len(query),
			"final_block_id": query[-1].block_id,
			"last_block_date": query[-1].block_date[0:19],
			"genesis_block_hash": query[0].block_hash,
			"final_block_data": query[-1].block_data
		}

		return render_template("main.html", context = info)

	else:
		return jsonify({"message" : "request is not valid"})
		
# add route - adding new blocks to the chain
@app.route("/add", methods = ["POST"])
def add_block():
	# add new block to the main blockchain
	if request.method == "POST":
		chain = Blockchain(database_instance = Chain)
		form_data = request.form["data"]
		data = form_data if form_data is not None else request.args.get("data")

		# new created block
		new_block = chain.hash_block(data = data)
		new_block_instance = Chain(block_id = new_block.block_id,
			block_hash = new_block.block_hash,
			block_data = new_block.block_data,
			block_date = new_block.block_date)

		db.session.add(new_block_instance)
		db.session.commit()

		return redirect(url_for("index"))

	else:
		return jsonify({"message" : "request is not valid"})