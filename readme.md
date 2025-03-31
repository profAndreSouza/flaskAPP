flask_api/
│── app/
│   ├── controllers/
│   │   ├── auth_controller.py
│   │   ├── user_controller.py
│   ├── models/
│   │   ├── user.py
│   ├── views/
│   │   ├── auth_routes.py
│   │   ├── user_routes.py
│   │   ├── graphql_routes.py
│   ├── schemas/
│   │   ├── user_schema.py
│   ├── __init__.py
│── config.py
│── main.py
│── requirements.txt
│── .env
│── migrations/




Criar ambiente virtual
python -m venv venv

Ativar o ambiente virtual
.\venv\Scripts\Activate

Instalar o Flask
pip install Flask

Para executar a aplicação (main.py)
flask --app main run