from flask import render_template, Blueprint, flash, redirect, url_for, request
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user
from application.models.users import User
from application.db import db

nonAuth = Blueprint('nonAuth', __name__)

@nonAuth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        remember = True if request.form.get('remember') else False
        
        print(email, password)
        
        user = User.query.filter_by(email=email).first()
        
        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again!')
            return redirect(url_for('nonAuth.login'))
        
        login_user(user, remember=remember)
        return redirect(url_for('auth.index'))

    return render_template('login.html')

@nonAuth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        
        existing_user = User.query.filter_by(email=email).first()
        
        if existing_user:
            flash('Email address already exists')
            return redirect(url_for('nonAuth.signup'))
        
        user = User(
            first_name = first_name,
            last_name = last_name,
            email = email,
            password = generate_password_hash(password, method='sha256')
        )
        
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('nonAuth.login'))

    return render_template('signup.html')