import os

class Config:
  SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://admin:admin@postgres:5432/projDB")
  SQLALCHEMY_TRACK_MODIFICATIONS = False

  JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "palmeiras-nao-tem-mundial-e-nem-os-gambas")

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