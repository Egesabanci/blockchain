import argparse
import requests

from src.app import cfg

parser = argparse.ArgumentParser()
parser.add_argument("--data", type = str, default = "No data.")
args = parser.parse_args()

host = cfg["host"]
port = cfg["port"]

# base request url
BASE = f"http://{host}:{port}/"

# add block with post request
def add_block() -> None:
	# post request to the "/add" route
	url = BASE + "/add"
	requests.post(url, data = {"data": args.data})

	return None

if __name__ == "__main__":
	add_block()