from flask import Blueprint
from flaskApp.app.controllers import auth_controller

auth_routes = Blueprint('auth_routes', __name__)

auth_routes.route('/auth/login', methods=['POST'])(auth_controller.login)
auth_routes.route('/auth/refresh', methods=['POST'])(auth_controller.refresh_token)