# Flask API

## Pré-requisitos

1. Python 3.12
2. Flask

## Configuração do Ambiente

### 1. Criar o Ambiente Virtual

Para isolar as dependências do projeto, crie um ambiente virtual:

```bash
python -m venv venv
```

### 2. Ativar o Ambiente Virtual

Ative o ambiente virtual:

- **No Windows**:

```bash
.\venv\Scripts\Activate
```

- **No macOS/Linux**:

```bash
source venv/bin/activate
```

### 3. Instalar as Dependências

Instale o Flask e outras dependências listadas em `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Executar a Aplicação

Para rodar a aplicação, use o seguinte comando:

```bash
flask --app main run
```

A aplicação estará disponível em `http://127.0.0.1:5000/` por padrão.


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
│   ├── __init__.py
│── config.py
│── main.py
│── requirements.txt
│── .env
│── migrations/
```

## Arquitetura

- **controllers/**: Contém os controladores responsáveis pela lógica de negócios, como autenticação e manipulação de usuários.
- **models/**: Contém os modelos que definem a estrutura dos dados (por exemplo, usuário).
- **views/**: Define as rotas e os endpoints da API (autenticação, usuários, etc).
- **schemas/**: Contém os esquemas de validação para as entradas da API.
- **config.py**: Arquivo de configuração da aplicação.
- **main.py**: Ponto de entrada principal para a execução da aplicação.
- **requirements.txt**: Lista de dependências do projeto.
- **.env**: Variáveis de ambiente sensíveis, como chaves secretas e configurações do banco de dados.
- **migrations/**: Contém arquivos de migração do banco de dados (se estiver utilizando algo como SQLAlchemy).
