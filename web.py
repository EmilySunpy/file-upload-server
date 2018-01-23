import json
import MySQLdb
import MySQLdb.cursors
from flask import Flask, render_template, url_for, request

import glob

app = Flask(__name__)

with open("config.json", "r") as f:
    glob.config = json.load(f)

glob.sql = MySQLdb.connect(**config["sql"], cursorclass = MySQLdb.cursors.DictCursor)

@app.route("/")
def serve_home():
    return "home"

@app.route("/register")
def serve_register():
    return "register"

@app.route("/{user}/")
def serve_userpage():
    return "userpage"

@app.route("/{user}/view/{file_ext}/{file_name}")
def serve_view_file():
    return "file viewer"

@app.route("/upload")
def handle_upload():
    return "upload"

if __name__ == "__main__":
    app.run(**glob.config["web"])