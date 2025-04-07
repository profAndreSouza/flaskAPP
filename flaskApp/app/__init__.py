from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flasgger import Swagger

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:admin@postgres:5432/projDB'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    ma.init_app(app)
    Swagger(app)

    from flaskApp.app.routes.user_routes import user_routes
    app.register_blueprint(user_routes)

    # Cria e popula o banco com mock
    with app.app_context():
        db.create_all()
        from flaskApp.app.seeders.seed import Seeder  
        Seeder().run()

    return app
