import os

class Config:
  JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "chave-secreta-para-assinar-e-verificar-a-autenticidade-dos-tokens-JWT")
  
  SESSION_TYPE = 'filesystem'

  SWAGGER_TEMPLATE = {
    "swagger": "2.0",
    "info": {
        "title": "Flask API",
        "version": "1.0"
    },
    "securityDefinitions": {
        "BearerAuth": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "Token JWT: Bearer {token}"
        }
    }
  }