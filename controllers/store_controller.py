from flask import Blueprint, jsonify
from services.store_service import StoreService

store_blueprint = Blueprint('stores', __name__)
store_service = StoreService()

@store_blueprint.route('/users/<int:user_id>/stores', methods=['GET'])
def get_stores_by_user(user_id):
    stores = store_service.get_stores_by_user(user_id)
    if not stores:
        return jsonify({'message': 'No stores found for this user'}), 404
    return jsonify([{'id': store.id, 'name': store.name} for store in stores])
