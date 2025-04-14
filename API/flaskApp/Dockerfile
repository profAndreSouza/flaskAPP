FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r flaskApp/requirements.txt

ENV PYTHONPATH=/app

EXPOSE 5000

CMD ["flask", "--app", "flaskApp.main", "run", "--host=0.0.0.0"]
