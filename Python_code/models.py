from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Myuser(db.Model):
    __tablename__ = 'myuser'
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(64))
    userid = db.Column(db.String(32))
    username = db.Column(db.String(8))

class LedTest(db.Model):
    __tablename__ = 'ledTable'
    id = db.Column(db.Integer, primary_key=True)
    red = db.Column(db.Integer)
    green = db.Column(db.Integer)
    yellow = db.Column(db.Integer)
    time = db.Column(db.String(30))