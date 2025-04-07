# Flask API

## Pré-requisitos

1. Python 3.12
2. Flask
3. Docker (opcional para banco de dados PostgreSQL)

## Configuração do Ambiente

### 1. Criar o Ambiente Virtual

```bash
python -m venv venv
```

### 2. Ativar o Ambiente Virtual

- **Windows**:
  ```bash
  .\venv\Scripts\activate
  ```

- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 3. Instalar as Dependências

```bash
pip install -r requirements.txt
```

### 4. Executar a Aplicação

```bash
flask --app main run
```

A aplicação estará disponível em `http://127.0.0.1:5000/`.

## Recursos da Aplicação

- **Autenticação JWT**: login, logout e refresh token
- **Seed de dados mockados** usando [Faker](https://faker.readthedocs.io/en/master/)
- **Criptografia de senhas** com `Werkzeug`
- **Documentação interativa** com **Swagger UI** via `flasgger`

> Acesse a documentação interativa em:  
> `http://127.0.0.1:5000/apidocs`

## Estrutura do Projeto

```
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
│   ├── seeders/
│   │   └── seed.py
│   ├── __init__.py
│── config.py
│── main.py
│── requirements.txt
│── .env
```

## Arquitetura

- **controllers/**: Regras de negócio (ex: autenticação, usuários).
- **models/**: Modelos do banco de dados.
- **schemas/**: Validações e serialização de dados com Marshmallow.
- **views/**: Arquivos de rotas/blueprints da aplicação.
- **seeders/**: Scripts de carga inicial de dados mockados.
- **config.py**: Configurações do app (ex: banco, JWT_SECRET).
- **main.py**: Ponto de entrada da aplicação Flask.