from flask import Blueprint, jsonify, abort
from services.user_service import UserService

user_blueprint = Blueprint('users', __name__)
user_service = UserService()

@user_blueprint.route('/users', methods=['GET'])
def get_users():
    users = user_service.get_all_users()
    return jsonify([{'id': user.id, 'name': user.name} for user in users])

@user_blueprint.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user_service.delete_user(user_id)
    return jsonify({'message': 'User deleted'})
