from flask import Blueprint, request, jsonify
from .models import User, Task
from . import db
from sqlalchemy.exc import IntegrityError
import datetime

api = Blueprint('api', __name__)

@api.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'User already exists'}), 400
    return jsonify({'id': new_user.id, 'username': new_user.username}), 201

@api.route('/users/<int:user_id>/tasks', methods=['POST'])
def create_task(user_id):
    data = request.get_json()
    task = Task(title=data['title'], description=data.get('description'), user_id=user_id)
    db.session.add(task)
    db.session.commit()
    return jsonify({'id': task.id, 'title': task.title}), 201

@api.route('/users/<int:user_id>/tasks', methods=['GET'])
def get_tasks(user_id):
    tasks = Task.query.filter_by(user_id=user_id).all()
    return jsonify([{
        'id': t.id,
        'title': t.title,
        'description': t.description,
        'completed': t.completed
    } for t in tasks])

@api.route('/tasks/<int:task_id>', methods=['PATCH'])
def update_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    data = request.get_json()
    if 'completed' in data:
        task.completed = data['completed']
    if 'title' in data:
        task.title = data['title']
    if 'description' in data:
        task.description = data['description']
    db.session.commit()
    return jsonify({'message': 'Task updated'})

@api.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted'})
