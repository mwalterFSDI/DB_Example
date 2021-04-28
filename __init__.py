#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Sample app"""

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.db"
db = SQLAlchemy(app)

from app.database import *

@app.route("/about/<int:uid>")
def about(uid):
    user = User.query.filter_by(id=uid).first()
    return render_template("about.html", user=user)

@app.route("/agent")
def agent():
    user_agent = request.headers.get("User-Agent")
    return "<p> Your user agent is: %s</p>" % user_agent

@app.route("/hello/<name>")
def hello(name):
    return render_template("hello.html", name=name)


