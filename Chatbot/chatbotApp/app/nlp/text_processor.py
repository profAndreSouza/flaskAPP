import re
import unicodedata

class TextPreProcessor:
    def preprocess(self, text):
        text = text.lower()
        text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('utf-8')
        text = re.sub(r'[^\w\s]', '', text)
        return text.strip()
