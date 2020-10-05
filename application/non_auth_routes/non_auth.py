from flask import render_template, Blueprint

nonAuth = Blueprint('nonAuth', __name__)

@nonAuth.route('/login')
def login():
    return render_template('login.html')

@nonAuth.route('/signup')
def signup():
    return render_template('signup.html')