import os
import configparser

config = configparser.ConfigParser()
folder = os.path.dirname(__file__)
file = os.path.abspath(os.path.join(folder, "..", "..", "development.ini"))

config.read(file)
main = config["app:nflpool"]
rollbar = config["rollbar:test_settings"]

settings = {**main, **rollbar}
