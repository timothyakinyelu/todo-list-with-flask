from ..db import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "users"
    
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
    )
    email = db.Column(
        db.String(255),
        unique=True,
        nullable=False
    )
    first_name = db.Column(
        db.String(255),
        nullable=False
    )
    last_name = db.Column(
        db.String(255),
        nullable=False
    )
    password = db.Column(
        db.String(100)
    )
    tasks = db.relationship(
        'Task', 
        backref='user', 
        lazy='joined'
    )