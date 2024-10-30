from flask import Blueprint, jsonify, request
from ..models.task import Task
from datetime import datetime

tasks_bp = Blueprint('tasks', __name__)

# Stockage temporaire (en mémoire; non-persistent)
tasks = []
task_id_counter = 1

@tasks_bp.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify([task.to_dict() for task in tasks])

@tasks_bp.route('/tasks', methods=['POST'])
def create_task():
    global task_id_counter
    data = request.get_json()

    if not data or 'title' not in data: 
        return jsonify({"error": "invalid information provided"})

    task = Task(
        title=data['title'],
        description=data.get('description', ''),
        status=data.get('status', 'todo')
    )
    task.id = task_id_counter
    task_id_counter += 1

    tasks.append(task)
    return jsonify(task.to_dict()), 201

@tasks_bp.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task.id == task_id), None)
    if task is None: 
        return jsonify({"error": "no task found"})
    return jsonify(task.to_dict())

@tasks_bp.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task.id == task_id), None)
    if task is None: 
        return jsonify({"error": "no task found"})

    data = request.get_json()
    if 'title' in data: 
        task.title = data['title']
    if 'description' in data: 
        task.description = data['description']
    if 'status' in data: 
        task.status = data['status']
    
    task.updated_at = datetime.now()
    return jsonify(task.to_dict())

@tasks_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = next((task for task in tasks if task.id == task_id), None)
    if task is None: 
        return jsonify({"error": "no task found"})
    
    tasks.remove(task)
    return jsonify({"message": "task removed"})
