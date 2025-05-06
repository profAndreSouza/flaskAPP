from app.nlp.text_processor import TextPreProcessor
from app.nlp.semantic_analyzer import SemanticAnalyzer

class NLPService:
    def __init__(self):
        self.preprocessor = TextPreProcessor()
        self.semantic = SemanticAnalyzer()

    def process_text(self, text: str) -> dict:
        clean = self.preprocessor.preprocess(text)
        intent, entities = self.semantic.extract_intent_and_entities(clean)
        return {
            "Intent": intent,
            "Entities": entities
        }
