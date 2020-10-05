import os
from flask import Flask
from flask_login import LoginManager
from application._helpers import load_config

def create_app():
    app = Flask(__name__, template_folder='./templates')
    mode = app.env
    Config = load_config(mode)
    app.config.from_object(Config)
    
    from .db import db
    db.init_app(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'nonAuth.login'
    login_manager.init_app(app)
    
    from .models.users import User
    from .models.task_types import TaskType
    from .models.tasks import Task
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    with app.app_context():
        # import non auth routes
        from .non_auth_routes.non_auth import nonAuth as non_auth_blueprint
        app.register_blueprint(non_auth_blueprint)
        
        # import auth routes
        from .auth_routes.auth import auth as auth_blueprint
        app.register_blueprint(auth_blueprint)
        
        db.create_all()
        
        return app
    
