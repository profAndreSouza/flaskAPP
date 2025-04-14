from flaskApp.app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    @property
    def password(self):
        raise AttributeError("Password is write-only.")

    @password.setter
    def password(self, plaintext_password):
        self.password_hash = generate_password_hash(plaintext_password)

    def check_password(self, plaintext_password):
        return check_password_hash(self.password_hash, plaintext_password)

    def __repr__(self):
        return f'<User {self.username}>'


# CREATE TABLE users (
# 	id SERIAL PRIMARY KEY,
# 	username VARCHAR(50) NOT NULL UNIQUE,
#     email VARCHAR(100) NOT NULL UNIQUE,
#     password_hash VARCHAR(100) NOT NULL
# );