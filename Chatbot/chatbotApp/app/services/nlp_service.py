from chatbotApp.app.nlp.text_processor import TextPreProcessor
from chatbotApp.app.nlp.semantic_analyzer import SemanticAnalyzer

class NLPService:
    def __init__(self):
        self.preprocessor = TextPreProcessor()
        self.semantic = SemanticAnalyzer()

    def process_text(self, text: str) -> dict:
        clean = self.preprocessor.preprocess(text)
        intent, entities = self.semantic.extract_intent_and_entities(clean)
        response = self.semantic.get_response(intent, entities, clean)

        # Decide o que fazer com base no tipo de resposta
        if isinstance(response, dict):
            if "answer" in response:
                final_response = response["answer"]
            elif "action" in response and response["action"] == "db":
                final_response = f"(Consulta API Banco: {response['target']} com {response['params']})"
            elif "fallback" in response:
                final_response = response["fallback"]
            else:
                final_response = "Resposta não encontrada."
        else:
            final_response = response

        return {
            "Intent": intent,
            "Entities": entities,
            "Response": final_response
        }
