from flask_sqlalchemy import SQLAlchemy

ledDB = SQLAlchemy()

class LedTable(ledDB.Model):
    __tablename__ = 'ledTable'
    red = ledDB.Column(ledDB.Integer)
    green = ledDB.Column(ledDB.Integer)
    yellow = ledDB.Column(ledDB.Integer)
    time = ledDB.Column(ledDB.String(30))