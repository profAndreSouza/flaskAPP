from flaskApp.app import db

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# CREATE TABLE users (
# 	id SERIAL PRIMARY KEY,
# 	username VARCHAR(50) NOT NULL UNIQUE,
#     email VARCHAR(100) NOT NULL UNIQUE,
#     password VARCHAR(100) NOT NULL
# );