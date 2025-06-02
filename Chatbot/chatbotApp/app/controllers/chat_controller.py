from flask import request, render_template, session, redirect, url_for, jsonify
from chatbotApp.app.services.gemini_service import GeminiService
from chatbotApp.app.services.nlp_service import NLPService
import json
import os


gemini_service = GeminiService()

def test():
    """
    Endpoint para retornar as respostas do NLP para as perguntas pré-definidas.

    ---
    tags:
      - Chatbot
    get:
      summary: Retorna respostas processadas para perguntas pré-definidas
      description: |
        Lê o arquivo de perguntas JSON e processa cada uma usando o serviço NLP,
        retornando uma lista JSON com pergunta, resposta e detalhes de NLP.
      responses:
        200:
          description: Lista de resultados com perguntas e respostas NLP
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    Pergunta:
                      type: string
                      description: Pergunta original
                    Resposta:
                      type: string
                      description: Resposta gerada pelo serviço NLP
                    NLP:
                      type: object
                      properties:
                        Intent:
                          type: string
                          description: Intenção identificada pelo NLP
                        Entities:
                          type: object
                          description: Entidades extraídas pelo NLP
    """

    questions_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'questions.json')
    
    with open(questions_path, 'r', encoding='utf-8') as f:
        questions = json.load(f)

    nlp = NLPService()
    gemini = GeminiService()

    results = []

    for prompt in questions:
        analysis = nlp.process_text(prompt)

        result = {
            "Pergunta": prompt,
            "Intent": analysis["Intent"],
            "Entities": analysis["Entities"],
            "Resposta": analysis["Response"]
        }

        results.append(result)

    return jsonify(results)


def chatbot():
    """
    Chat endpoint
    ---
    tags:
      - Chatbot
    get:
      description: Render chat page with history
      responses:
        200:
          description: Chat page
    post:
      description: Send a message to the chatbot
      parameters:
        - name: message
          in: formData
          type: string
          required: true
          description: User message to send to chatbot
      responses:
        302:
          description: Redirect to chat page after message
    """
    if "chat_history" not in session:
        session["chat_history"] = []

    if request.method == "POST":
        user_input = request.form.get("message")
        if user_input:
            bot_response = gemini_service.get_response_html(user_input)
            
            session["chat_history"].append({"user": user_input, "bot": bot_response})
            session.modified = True

        return redirect(url_for("chatbot.chatbot"))

    return render_template("index.html", chat_history=session["chat_history"])