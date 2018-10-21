from flask import Flask, render_template
from flask_heroku import Heroku
from flask_sqlalchemy import SQLAlchemy
import sys
import json



app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
heroku = Heroku(app)
db = SQLAlchemy(app)

@app.route("/")
def main():
    return render_template("IndexPage.html")

if __name__=="__main__":
    aport = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)