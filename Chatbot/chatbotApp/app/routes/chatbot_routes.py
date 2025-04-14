from flask import Blueprint
from app.controllers import chat_controller

chatbot_bp = Blueprint('chatbot', __name__)

chatbot_bp.route("/chat/", methods=['GET', 'POST'])(chat_controller.chatbot)