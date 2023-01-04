import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://postgres:postgres@db:5432/postgres"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))

    def __init__(self, id, firstname, lastname):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname

    def __repr__(self):
        return f"{self.id} | {self.firstname} | {self.lastname}"


@app.route("/")
def home():
    return render_template("nav.html")



@app.route("/users")
def api():
    list = Users.query.all()
    return render_template("data_table.html", list=list)


if __name__ == "__main__":
    app.run(debug=True)
