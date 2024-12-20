import datetime as datetime
from DataBase.config import  db

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True),
    username = db.Column(db.Sting(50), unique=True, nullable=False),
    emial = db.Column(db.String(100), unique=True, nullable=False),
    password = db.Column(db.Sting, nullable=False),
    created_at = db.Column(db.DateTime, default=datetime.datetime.now),
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now)