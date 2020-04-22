from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "test_users"
    FullName = db.Column(db.String(120), nullable = False)
    username = db.Column(db.String(80), primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120), unique=True)




    