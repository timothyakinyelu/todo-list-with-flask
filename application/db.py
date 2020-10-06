from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import force_auto_coercion

db = SQLAlchemy()
session = db.session