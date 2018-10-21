from flask import Flask, render_template, request, flash, redirect,  url_for
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku
from flask_sqlalchemy import SQLAlchemy
import sys
import json

import logging

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
heroku = Heroku(app)
db = SQLAlchemy(app)

@app.route("/", methods=["GET"])
def main():
    return render_template("indexPage.html")
@app.route("/register.html", methods=["GET", "POST"])
def register():
    if request.method == "POST": #if user actually posted
       name = request.form["username"]
       logging.info(name)
       return redirect(url_for("showlogin"))
    #else return the register page   
    return render_template("register.html")

@app.route("/login.html", methods=["GET"])
def showlogin():
    #if user posted
    name = request.args.get("username")
    return render_template("signin.html")

@app.route("/login.html", methods=["GET", "POST"])
def login():
    if request.method == "POST": # if user posted
        name = request.form["username"]
        return redirect(url_for("homepage"))
    return render_template("signin.html") 

@app.route("/home.html", methods=["GET"])
def homepage():
    return render_template("home.html")
       


if __name__ == "__main__":
    print 
    app.run()


