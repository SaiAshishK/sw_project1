from flask import Flask
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from models import *

# Settings
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://hmlzedxmyiixoc:881761f4937ebeaaba755f03aec7f8f4449d2f0ad0d35f8ac78019e371ae9499@ec2-18-210-214-86.compute-1.amazonaws.com:5432/dekf5v3rogk5p2"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()