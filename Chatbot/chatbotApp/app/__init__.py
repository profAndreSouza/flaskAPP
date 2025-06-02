from flask import Flask
from flask_session import Session
from flasgger import Swagger
from chatbotApp.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    Swagger(app, template=Config.SWAGGER_TEMPLATE)
    Session(app)

    from chatbotApp.app.routes.chatbot_routes import chatbot_bp
    app.register_blueprint(chatbot_bp)
    
    return app
