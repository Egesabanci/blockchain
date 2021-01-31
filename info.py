import argparse
import requests

from src.app import cfg

# parser for all command-line inputs
parser = argparse.ArgumentParser()
parser.add_argument("--num_blocks", action = "store_true")
parser.add_argument("--final_id", action = "store_true")
parser.add_argument("--final_hash", action = "store_true")
parser.add_argument("--final_data", action = "store_true")
parser.add_argument("--final_date", action = "store_true")
parser.add_argument("--genesis_hash", action = "store_true")
parser.add_argument("--genesis_date", action = "store_true")
args = parser.parse_args()

host = cfg["host"]
port = cfg["port"]

# base request url
BASE = f"http://{host}:{port}/"

def get_info() -> None:
	url = BASE + "/get_info"
	res = requests.get(url).json()

	if args.num_blocks:
		print("Number of Blocks:", res["num_of_blocks"])

	if args.final_id:
		print("Final Block's ID:", res["final_block_id"])

	if args.final_hash:
		print("Final Block's Hash:", res["final_block_hash"])

	if args.final_data:
		print("Final Block's Data:", res["final_block_data"])

	if args.final_date:
		print("Number of Blocks:", res["last_block_date"])

	if args.genesis_hash:
		print("Genesis Block's Hash:", res["genesis_block_hash"])

	if args.genesis_date:
		print("Genesis Block's Date:", res["genesis_block_date"])

	return None

if __name__ == "__main__":
	get_info()