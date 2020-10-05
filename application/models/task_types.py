from ..db import db

class TaskType(db.Model):
    __tablename__ = "task_types"
    
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    name = db.Column(
        db.String(100),
        nullable=False
    )
    tasks = db.relationship(
        'Task', 
        backref='task_type', 
        lazy='joined'
    )