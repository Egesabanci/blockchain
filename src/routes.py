from flask import request, render_template

from .app import app
from .database import db
from .models import Blockchain

# index route - serving main.html, get chain info
@app.route("/", methods = ["GET", "POST"])
def index():
	if request.method == "GET":
		return render_template("main.html")
		
# add route - adding new blocks to the chain
@app.route("/add", methods = ["POST"])
def add_block():
	pass