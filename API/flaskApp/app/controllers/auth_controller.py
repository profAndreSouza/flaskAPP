from datetime import timedelta
from flask import request, jsonify
from flask_jwt_extended import (
    create_access_token, create_refresh_token,
    jwt_required, get_jwt_identity
)
from flaskApp.app.models.user import User

ACCESS_EXPIRES = timedelta(minutes=15)
REFRESH_EXPIRES = timedelta(days=1)

def login():
    """
    Realiza o login do usuário e retorna tokens JWT
    ---
    tags:
      - Autenticação
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - email
            - password
          properties:
            email:
              type: string
              example: usuario@email.com
            password:
              type: string
              example: senha123
    responses:
      200:
        description: Login bem-sucedido
        schema:
          type: object
          properties:
            access_token:
              type: string
            refresh_token:
              type: string
      401:
        description: Credenciais inválidas
    """
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        access_token = create_access_token(
            identity=str(user.id),
            expires_delta=ACCESS_EXPIRES
        )
        refresh_token = create_refresh_token(
            identity=str(user.id),
            expires_delta=REFRESH_EXPIRES
        )
        return jsonify({
            "access_token": access_token,
            "refresh_token": refresh_token
        }), 200
    return jsonify({"error":"Credenciais inválidas"}), 401

@jwt_required(refresh=True)
def refresh_token():
    """
    Gera um novo token de acesso usando o refresh token
    ---
    tags:
      - Autenticação
    security:
      - BearerAuth: []
    responses:
      200:
        description: Novo token de acesso gerado
        schema:
          type: object
          properties:
            access_token:
              type: string
    """
    user_id = get_jwt_identity()
    new_token = create_access_token(
        identity=str(user_id),
        expires_delta=ACCESS_EXPIRES
    )
    return jsonify(access_token=new_token), 200
