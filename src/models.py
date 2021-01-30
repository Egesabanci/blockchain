import datetime.datetime as time
from uuid import uuid4

from .database import db

# main database model - blockchain class
class Blockchain(db.Model):
	block_number = db.Column(db.Integer, primary_key = True)
	block_id		 = db.Column(db.String(32), unique = True, nullable = False, default = uuid4().hex)
	block_hash	 = db.Column(db.String(64), unique = True, nullable = False)
	block_data	 = db.Column(db.String(255), nullable = False)
	block_date 	 = db.Column(db.String(26), default = time.now())

	def __repr__(self):
		return f"<Block {self.block_id}>"