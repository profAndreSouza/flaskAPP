from flask import Blueprint
from flaskApp.app.controllers import query_controller

query_routes = Blueprint('query_routes', __name__)

query_routes.route('/query', methods=['POST'])(query_controller.query)
