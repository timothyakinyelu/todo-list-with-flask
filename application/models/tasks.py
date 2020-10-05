from ..db import db

class Task(db.Model):
    __tablename__ = "tasks"
    
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    task_type_id = db.Column(
        db.Integer,
        db.ForeignKey('task_types.id'),
        nullable=False
    )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id')
    )
    title = db.Column(
        db.String(100),
        nullable=False
    )
    content = db.Column(
        db.Text,
        nullable=False
    )
    priority = db.Column(
        db.String(100),
        nullable=False,
        server_default="LOW"
    )
    completed = db.Column(
        db.Boolean,
        server_default="0"
    )
    date_created  = db.Column(
        db.DateTime,  
        default=db.func.current_timestamp()
    )
    date_modified = db.Column(
        db.DateTime,  
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp()
    )
    