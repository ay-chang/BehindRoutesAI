from flask import Blueprint, request, jsonify
from .models import User, USERS_DB

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "Welcome to the Flask Sample Project!"

@main.route('/users', methods=['GET'])
def get_users():
    return jsonify([user.to_dict() for user in USERS_DB])

@main.route('/users', methods=['POST'])
def add_user():
    data = request.json
    new_user = User(name=data['name'], email=data['email'])
    USERS_DB.append(new_user)
    return jsonify(new_user.to_dict()), 201
