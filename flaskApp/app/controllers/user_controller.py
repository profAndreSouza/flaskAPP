from flask import request, jsonify
from flaskApp.app.models.user import User
from flaskApp.app.schemas.user_schema import UserSchema
from flaskApp.app import db

# Create a new user
def create_user():
    try:
        user_data = request.get_json()
        user_schema = UserSchema()
        user = user_schema.load(user_data)
        db.session.add(user)
        db.session.commit()
        return jsonify(user_schema.dump(user)), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Get all users
def get_users():
    users = User.query.all()
    user_schema = UserSchema(many=True)
    return jsonify(user_schema.dump(users)), 200

# Get user by ID
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        user_schema = UserSchema()
        return jsonify(user_schema.dump(user)), 200
    return jsonify({"error": "User not found"}), 404

# Update user by ID
def update_user(user_id):
    user = User.query.get(user_id)
    if user:
        user_data = request.get_json()
        user_schema = UserSchema()
        user = user_schema.load(user_data, instance=user, partial=True)
        db.session.commit()
        return jsonify(user_schema.dump(user)), 200
    return jsonify({"error": "User not found"}), 404

# Delete user by ID
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted"}), 200
    return jsonify({"error": "User not found"}), 404
