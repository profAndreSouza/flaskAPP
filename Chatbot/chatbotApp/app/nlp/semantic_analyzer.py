import os
import json
import re
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

        if response:
            try:
                return response.format(**entities)
            except KeyError:
                return response  # retorna mesmo se faltar entidade
        elif intent in self.knowledge.get("fallback_database", []):
            return self._query_database(intent, entities)
        elif intent == "intencao_desconhecida":
            return self._ask_ai(text)
        else:
            return (
                f"Não encontrei uma resposta pronta para a intenção '{intent}'. "
                "Consultando fontes alternativas para te ajudar melhor."
            )



    def _query_database(self, entities):
        # Chamada simulada para API de banco de dados
        # Exemplo: número de peças nas últimas 24h
        return f"consultar_quantidade_produzida(entities)"

    def _ask_ai(self, text):
        # Chamada real para a IA (Gemini, GPT, etc.)
        from chatbotApp.app.services.gemini_service import GeminiService
        gemini = GeminiService()
        return gemini.get_response(text)

