FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r chatbotApp/requirements.txt

RUN python -m spacy download pt_core_news_sm

ENV PYTHONPATH=/app

EXPOSE 5001

CMD ["flask", "--app", "chatbotApp.main", "run", "--host=0.0.0.0", "--port=5001"]
