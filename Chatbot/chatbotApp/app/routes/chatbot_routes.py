from flask import Blueprint, request, render_template

chatbot_bp = Blueprint('chatbot', __name__)

@chatbot_bp.route("/", methods=['GET', 'POST'])
def chat():
    return "hello world!"