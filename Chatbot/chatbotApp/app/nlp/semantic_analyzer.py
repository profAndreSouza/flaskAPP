import os
import json
import re
import requests
from chatbotApp.app.nlp.syntatic_analyzer import SyntaticAnalyzer


class SemanticAnalyzer:
    def __init__(self, knowledge_path=""):
        if knowledge_path == "":
            knowledge_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'knowledge.json')
        self.syntactic = SyntaticAnalyzer()
        self.knowledge = self._load_knowledge(knowledge_path)

    def _load_knowledge(self, path):
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    def extract_intent_and_entities(self, text):
        """Retorna a intenção detectada e entidades extraídas do texto."""
        text = text.lower()
        pos_tags = self.syntactic.analyze(text)
        intent = self._detect_intent(text)
        entities = self._extract_entities(text)
        return intent, entities

    def _detect_intent(self, text):
        for intent_name, config in self.knowledge.get("intents", {}).items():
            for keyword in config.get("keywords", []):
                if keyword.lower() in text:
                    return intent_name
        return "intencao_desconhecida"

    def _extract_entities(self, text):
        extracted = {}
        for entity_name, config in self.knowledge.get("entities", {}).items():
            patterns = config.get("patterns", [])
            group = config.get("grupo")

            for pattern in patterns:
                match = re.search(pattern, text)
                if match:
                    if group is not None:
                        extracted[entity_name] = match.group(int(group))
                    else:
                        extracted[entity_name] = match.group(0) if match.groups() else True
                    break  # Apenas a primeira correspondência é usada
        return extracted

    def get_response(self, intent, entities, text):
        """Retorna a resposta da base de conhecimento, do banco ou da IA."""
        intents_knowledge = self.knowledge.get("intents", {})
        response = intents_knowledge.get(intent, {}).get("response")
        action = intents_knowledge.get(intent, {}).get("action")

        if response:
            try:
                return response.format(**entities)
            except KeyError:
                return response
        elif action:
            return self._query_database(action, entities)
        elif intent == "intencao_desconhecida":
            return self._ask_ai(text)
        else:
            return (
                f"Não encontrei uma resposta pronta para a intenção '{intent}'. "
                "Consultando fontes alternativas para te ajudar melhor."
            )

    def _query_database(self, action, entities):

        clean_action = action.replace("API_DB_QUERY::", "")
        payload = {
            "action": clean_action,
            "entities": entities
        }

        try:
            response = requests.post(f"http://localhost:5000/query", json=payload)
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"Erro na consulta: {response.status_code}", "details": response.text}

        except requests.exceptions.RequestException as e:
            return {"error": "Erro ao conectar com a API de consulta", "details": str(e)}

    def _ask_ai(self, text):
        # Chamada real para a IA (Gemini, GPT, etc.)
        from chatbotApp.app.services.gemini_service import GeminiService
        gemini = GeminiService()
        return gemini.get_response(text)

