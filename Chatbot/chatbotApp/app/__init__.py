from flask import Flask
from app.routes.chatbot_routes import chatbot_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(chatbot_bp)
    app.secret_key = "sua_chave_super_secreta"

    
    return app