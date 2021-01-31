from src.app import app
from src.app import cfg

# run the server
if __name__ == "__main__":
	app.run(host = cfg["host"],
		port = cfg["port"],
		debug = cfg["debug"])