import os
import yaml

from src.app import app
from src.database import db

# read configurations
with open(os.path.join("src", "config.yml"), "r") as config:
	cfg = yaml.safe_load(config)["config"]

# run the server
if __name__ == "__main__":
	app.run(host = cfg["host"], port = cfg["port"])