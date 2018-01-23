import json
import MySQLdb
import MySQLdb.cursors
from flask import Flask, render_template, url_for, request

from handlers import upload_handler

import glob

app = Flask(__name__)

with open("config.json", "r") as f:
    glob.config = json.load(f)

glob.sql = MySQLdb.connect(**glob.config["sql"], cursorclass = MySQLdb.cursors.DictCursor)

def cache_users():
    cursor = glob.sql.cursor()
    cursor.execute("SELECT username,password FROM users WHERE locked = 0")
    rows = cursor.fetchall()
    for row in rows:
        glob.users[row["username"]] = row["password"]

@app.route("/")
def serve_home():
    return "home"

@app.route("/register")
def serve_register():
    return "register"

@app.route("/<user>/")
def serve_userpage(user):
    return "userpage"

@app.route("/<user>/view/<file_ext>/<file_name>")
def serve_view_file(user, file_ext, file_name):
    return "file viewer"

@app.route("/upload")
def handle_upload():
    return upload_handler.upload(request)

if __name__ == "__main__":
    cache_users()
    app.run(**glob.config["web"])