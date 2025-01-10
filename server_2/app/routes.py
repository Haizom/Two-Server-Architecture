from flask import Blueprint, render_template, request, redirect, url_for, flash
import requests

web_bp = Blueprint('web', __name__)

# URL of Server 1
SERVER_1_URL = 'http://127.0.0.1:5000'

@web_bp.route('/')
def index():
    return render_template('register.html')

@web_bp.route('/login')
def login_page():
    return render_template('login.html')

@web_bp.route('/register', methods=['POST'])
def register_user():
    name = request.form.get('name')
    email = request.form.get('email')
    age = request.form.get('age')
    password = request.form.get('password')

    if not name or not email or not age or not password:
        flash('All fields are required!', 'error')
        return redirect(url_for('web.index'))

    response = requests.post(f'{SERVER_1_URL}/user', json={"name": name, "email": email, "age": age, "password": password})

    if response.status_code == 201:
        flash('User registered successfully!', 'success')
    else:
        flash(response.json().get('error', 'Error registering user'), 'error')

    return redirect(url_for('web.index'))

@web_bp.route('/login', methods=['POST'])
def login_user():
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        flash('Email and password are required!', 'error')
        return redirect(url_for('web.login_page'))

    response = requests.post(f'{SERVER_1_URL}/user/login', json={"email": email, "password": password})

    if response.status_code == 200:
        user = response.json().get('user')
        return render_template('user_profile.html', user=user)
    else:
        flash(response.json().get('error', 'Login failed'), 'error')
        return redirect(url_for('web.login_page'))

@web_bp.route('/user/<uid>', methods=['GET'])
def get_user(uid):
    response = requests.get(f'{SERVER_1_URL}/user/{uid}')
    
    if response.status_code == 200:
        user = response.json()
        return render_template('user_profile.html', user=user)
    else:
        flash(response.json().get('error', 'User not found'), 'error')
        return redirect(url_for('web.index'))
