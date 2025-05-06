from flask import Flask, jsonify
from app import create_app
from app.services.nlp_service import NLPService
from app.services.gemini_service import GeminiService
import json

app = create_app()

@app.route('/')
def index():
    # Lê o arquivo de perguntas
    with open('app/data/questions.json', 'r', encoding='utf-8') as f:
        questions = json.load(f)

    nlp = NLPService()
    gemini = GeminiService()

    results = []

    for prompt in questions:
        nlp_result = nlp.process_text(prompt)
        gemini_result = gemini.get_response_json(prompt)

        result = {
            "Original": prompt,
            "NLP": {
                "Intent": nlp_result["Intent"],
                "Entities": nlp_result["Entities"]
            }
        }

        if "erro" in gemini_result:
            result["Gemini"] = {
                "Erro": gemini_result["Erro"],
                "Resposta": gemini_result.get("Resposta", "desconhecida")
            }
        else:
            result["Gemini"] = {
                "Intent": gemini_result.get("Intent", "desconhecida"),
                "Entities": gemini_result.get("Entities", {})
            }

        results.append(result)

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
