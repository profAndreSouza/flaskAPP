FROM python:3.12

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia todos os arquivos do projeto para o contêiner
COPY . .

# Instala as dependências listadas no requirements.txt
RUN pip install --no-cache-dir -r ./flaskApp/requirements.txt

# Expõe a porta 5000 para acesso externo
EXPOSE 5000

# Define o comando de inicialização da aplicação Flask
CMD ["flask", "--app", "flaskApp.main", "run", "--host=0.0.0.0"]
