from flask import Blueprint
from flaskApp.app.controllers import user_controller

user_routes = Blueprint('user_routes', __name__)

user_routes.route('/users', methods=['POST'])(user_controller.create_user)
user_routes.route('/users', methods=['GET'])(user_controller.get_users)
user_routes.route('/users/<int:user_id>', methods=['GET'])(user_controller.get_user)
user_routes.route('/users/<int:user_id>', methods=['PUT'])(user_controller.update_user)
user_routes.route('/users/<int:user_id>', methods=['DELETE'])(user_controller.delete_user)
