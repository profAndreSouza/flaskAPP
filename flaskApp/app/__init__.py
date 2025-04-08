from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flasgger import Swagger
from flaskApp.config import Config
from flask_jwt_extended import JWTManager

jwt = JWTManager()
db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    Swagger(app, template=Config.SWAGGER_TEMPLATE)

    from flaskApp.app.routes.user_routes import user_routes
    from flaskApp.app.routes.auth_routes import auth_routes
    
    app.register_blueprint(user_routes)
    app.register_blueprint(auth_routes)

    # Cria e popula o banco com mock
    with app.app_context():
        db.create_all()
        from flaskApp.app.seeders.seed import Seeder  
        Seeder().run()

    return app
