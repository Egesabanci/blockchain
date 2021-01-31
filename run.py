import argparse

from src.app import app
from src.app import cfg
from src.database import db

parser = argparse.ArgumentParser()
parser.add_argument("--host", type = str)
parser.add_argument("--port", type = int)
args = parser.parse_args()

# runserver configuration
host = cfg["host"] if args.host is None else args.host
port = cfg["port"] if args.port is None else args.port

# run the server
if __name__ == "__main__":
	app.run(host = host,
		port = port,
		debug = cfg["debug"])