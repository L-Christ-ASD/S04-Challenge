from datetime import datetime

class User:
    def __init__(self, username):
        self.id = None # sera défini lors de l'ajout à la liste
        self.username = username
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        return {
            "id": self.id,
            "from flask import Blueprint, jsonify, request
from ..models.user import User

users_bp = Blueprint('users', __name__)

# Stocke la donnée en mémoire (TEMPORAIRE!)
users = []
user_id_ctr = 1

@users_bp.route('/users', methods=['GET'])
def get_users():
    return jsonify([user.to_dict() for user in users])

@users_bp.route('/users', methods=['POST'])
def create_users():
    global user_id_ctr
    data = request.get_json()

    if not data or 'username' not in data: 
        return jsonify({"error": "username is required is request body!"}), 400

    user = User(username=data['username'])
    user.id = user_id_ctr
    user_id_ctr += 1

    users.append(user)
    return jsonify(user.to_dict()), 201": self.username,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }