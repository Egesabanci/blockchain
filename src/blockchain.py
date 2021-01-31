from uuid import uuid4
from hashlib import sha256
from datetime import datetime


class Block(object):

	def __init__(self, block_id: str, block_hash: str,
		block_data: str, block_date: str):

		self.block_id = block_id
		self.block_hash = block_hash
		self.block_data = block_data
		self.block_date = block_date


class Blockchain(object):

	def __init__(self, database_instance):
		self.database = database_instance

	def genesis(self):
		# created genesis block
		genesis_block = Block(block_id = uuid4().hex,
			block_hash = sha256(bytes("0", encoding = "utf-8")).hexdigest(),
			block_data = "created by egesabanci",
			block_date = str(datetime.now()))

		return genesis_block

	def previous_hash(self):
		return self.database.query.all()[-1].block_hash

	def hash_block(self, data):
		# hashing block with given data
		previous_hash = self.previous_hash()
		block_id = uuid4().hex
		block_date = str(datetime.now())

		hash_instance = str(previous_hash + block_id + data + block_date)
		final_hash = sha256(bytes(hash_instance, encoding = "utf-8")).hexdigest()

		# new block with hashed special fingerprint
		new_block = Block(block_id = block_id,
			block_hash = final_hash,
			block_data = data,
			block_date = block_date)

		return new_block