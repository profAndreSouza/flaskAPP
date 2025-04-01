from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Inicializando os objetos globais
db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)

    # Configuração do banco de dados PostgreSQL
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:admin@postgres:5432/projDB'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializando o banco de dados e Marshmallow
    db.init_app(app)
    ma.init_app(app)

    # Registrando as rotas
    from flaskApp.app.routes.user_routes import user_routes
    app.register_blueprint(user_routes)

    return app
