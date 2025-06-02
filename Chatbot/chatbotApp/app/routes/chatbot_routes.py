from flask import Blueprint
from chatbotApp.app.controllers import chat_controller

chatbot_bp = Blueprint('chatbot', __name__)

chatbot_bp.route("/chat/test", methods=["GET"])(chat_controller.test)
chatbot_bp.route("/chat/", methods=["GET", "POST"])(chat_controller.chatbot)
