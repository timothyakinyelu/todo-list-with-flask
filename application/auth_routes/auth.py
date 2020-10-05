from flask import render_template, Blueprint, redirect, url_for
from flask_login import login_required

auth = Blueprint('auth', __name__)

@auth.route('/')
@login_required
def index():
    render_template('index.html')
    
@auth.route('/todos-detail', methods=['GET', 'POST'])
@login_required
def taskDetails():
    render_template('todo-detail.html')