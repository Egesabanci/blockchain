import os
import argparse

# get flags from command line
parser = argparse.ArgumentParser()
parser.add_argument("--venv", action = "store_true")
args = parser.parse_args()


class BuildPipelines(object):

	@staticmethod
	def with_env() -> None:
		# download virtual environment library
		os.system("pip install virtualenv")

		# create virtual environment on base directory 
		BASE = os.path.dirname(os.getcwd())
		os.chdir(BASE)
		os.system("virtualenv .")
		os.system("cd Scripts")
		os.system("activate")
		os.system("cd ..")

		# download requirements
		os.system("pip install -r requirements.txt")

		return None

	@staticmethod
	def without_env() -> None:
		# install requirements
		os.system("pip install -r requirements.txt")

		return None


if __name__ == "__main__":
	# build scripts
	if args.venv:
		BuildPipelines.with_env()
	else:
		BuildPipelines.without_env()