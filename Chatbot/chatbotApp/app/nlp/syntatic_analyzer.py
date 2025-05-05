import spacy

class SyntaticAnalyzer:
    def __init__(self):
        self.nlp = spacy.load("pt_core_news_sm")

    def analyze(self, text):
        doc = self.nlp(text)
        return [(token.text, token.pos_) for token in doc]
    
