from flask import Flask
from app.routes.chatbot_routes import chatbot_bp
from flask_session import Session

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = "palmeiras_nao_tem_mundial"
    app.config['SESSION_TYPE'] = 'filesystem'
    Session(app)

    app.register_blueprint(chatbot_bp)
    
    return app