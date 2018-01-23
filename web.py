import json
import MySQLdb
import MySQLdb.cursors
from flask import Flask, render_template, url_for, request

import glob

app = Flask(__name__)

with open("config.json", "r") as f:
    glob.config = json.load(f)

if __name__ == "__main__":
    app.run(**glob.config["web"])