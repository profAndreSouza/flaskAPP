from flask import request, jsonify
from flask_jwt_extended import jwt_required
from flaskApp.app.models.user import User
from flaskApp.app.schemas.user_schema import UserSchema
from flaskApp.app import db

# Create a new user
@jwt_required()
def create_user():
    """
    Cria um novo usuário
    ---
    tags:
      - Usuários
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - username
            - email
            - password
          properties:
            username:
              type: string
              example: ana.paula
            email:
              type: string
              example: ana@example.com
            password:
              type: string
              example: 123456
    responses:
      201:
        description: Usuário criado com sucesso
        schema:
          type: object
          properties:
            id:
              type: integer
            username:
              type: string
            email:
              type: string
      400:
        description: Erro ao criar usuário
    """
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
    """
    Retorna todos os usuários
    ---
    tags:
      - Usuários
    responses:
      200:
        description: Lista de usuários
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              username:
                type: string
              email:
                type: string
    """
    users = User.query.all()
    user_schema = UserSchema(many=True)
    return jsonify(user_schema.dump(users)), 200

# Get user by ID
@jwt_required()
def get_user(user_id):
    """
    Retorna um usuário pelo ID
    ---
    tags:
      - Usuários
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: ID do usuário
    responses:
      200:
        description: Usuário encontrado
        schema:
          type: object
          properties:
            id:
              type: integer
            username:
              type: string
            email:
              type: string
      404:
        description: Usuário não encontrado
    """
    user = User.query.get(user_id)
    if user:
        user_schema = UserSchema()
        return jsonify(user_schema.dump(user)), 200
    return jsonify({"error": "User not found"}), 404

# Update user by ID
@jwt_required()
def update_user(user_id):
    """
    Atualiza um usuário pelo ID
    ---
    tags:
      - Usuários
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            username:
              type: string
              example: novo.usuario
            email:
              type: string
              example: novo@example.com
            password:
              type: string
              example: nova_senha
    responses:
      200:
        description: Usuário atualizado
        schema:
          type: object
          properties:
            id:
              type: integer
            username:
              type: string
            email:
              type: string
      404:
        description: Usuário não encontrado
    """
    user = User.query.get(user_id)
    if user:
        user_data = request.get_json()
        user_schema = UserSchema()
        user = user_schema.load(user_data, instance=user, partial=True)
        db.session.commit()
        return jsonify(user_schema.dump(user)), 200
    return jsonify({"error": "User not found"}), 404

# Delete user by ID
@jwt_required()
def delete_user(user_id):
    """
    Deleta um usuário pelo ID
    ---
    tags:
      - Usuários
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Usuário deletado
        schema:
          type: object
          properties:
            message:
              type: string
              example: User deleted
      404:
        description: Usuário não encontrado
    """
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted"}), 200
    return jsonify({"error": "User not found"}), 404
