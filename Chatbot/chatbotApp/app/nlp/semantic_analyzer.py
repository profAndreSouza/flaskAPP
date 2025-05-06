from app.nlp.syntatic_analyzer import SyntaticAnalyzer
import json
import re

class SemanticAnalyzer:
    def __init__(self, intents_path="app/data/intents.json", entities_path="app/data/entities.json"):
        self.syntactic = SyntaticAnalyzer()
        with open(intents_path, "r", encoding="utf-8") as f:
            self.intents = json.load(f)
        with open(entities_path, "r", encoding="utf-8") as f:
            self.entities = json.load(f)

    def extract_intent_and_entities(self, text):
        pos_tags = self.syntactic.analyze(text)
        intent = self.detect_intent(text, pos_tags)
        entities = self.extract_entities(text, pos_tags)
        return intent, entities

    def detect_intent(self, text, pos_tags):
        for intent, keywords in self.intents.items():
            for keyword in keywords:
                if keyword in text:
                    return intent
        return "intencao_desconhecida"


    def extract_entities(self, text, pos_tags):
        extracted = {}
        for entity, config in self.entities.items():
            patterns = config["patterns"]
            group = config.get("grupo", None)

            for pattern in patterns:
                match = re.search(pattern, text)
                if match:
                    if group is not None:
                        extracted[entity] = match.group(int(group))
                    else:
                        extracted[entity] = True
                    break
        return extracted
