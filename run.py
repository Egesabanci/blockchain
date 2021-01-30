import argparse

from src.app import app
from src.app import cfg
from src.database import db

parser = argparse.ArgumentParser()
parser.add_argument("--custom", action = "store_true")
parser.add_argument("--host", type = str)
parser.add_argument("--port", type = int)
args = parser.parse_args()

# runserver configuration
host = cfg["host"]
port = cfg["port"] 

# if added custom arguments from commandline
if args.custom:
	host = args.host
	port = args.port

# run the server
if __name__ == "__main__":
	app.run(host = host,
		port = port,
		debug = cfg["debug"])