from flask import Blueprint, request, jsonify
from .services import add_user_service, get_user_service, update_user_service, delete_user_service, login_user_service

user_bp = Blueprint('user', __name__)

@user_bp.route('/user', methods=['POST'])
def add_user():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    age = data.get('age')
    password = data.get('password')

    if not name or not email or not age or not password:
        return jsonify({"error": "Name, email, age, and password are required"}), 400

    result, status_code = add_user_service(name, email, age, password)
    return jsonify(result), status_code

@user_bp.route('/user/login', methods=['POST'])
def login_user():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    result, status_code = login_user_service(email, password)
    return jsonify(result), status_code

@user_bp.route('/user/<uid>', methods=['GET'])
def get_user(uid):
    result, status_code = get_user_service(uid)
    return jsonify(result), status_code

@user_bp.route('/user/<uid>', methods=['PUT'])
def update_user(uid):
    data = request.json
    age = data.get('age')

    if not age:
        return jsonify({"error": "Age is required to update profile"}), 400

    result, status_code = update_user_service(uid, age)
    return jsonify(result), status_code

@user_bp.route('/user/<uid>', methods=['DELETE'])
def delete_user(uid):
    result, status_code = delete_user_service(uid)
    return jsonify(result), status_code
