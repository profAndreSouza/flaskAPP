import os
import re
import json
import markdown
from dotenv import load_dotenv
import google.generativeai as genai
from google.api_core.exceptions import GoogleAPIError

class GeminiService:
    _instance = None 

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GeminiService, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return 

        load_dotenv()
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("A variável de ambiente GOOGLE_API_KEY não está definida.")

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-pro")
        self.chat_session = self.model.start_chat(history=[])

        self._initialized = True 

    def _build_prompt(self, user_input: str) -> str:
        return f"""
        Processar a seguinte entrada usando PNL. Extraia as entidades e a intenção com base no texto abaixo e retorne no formato JSON como mostrado abaixo:
        
        Entrada: "{user_input}"

        Saída esperada:
        {{
            "Entities": {{
                "material": true
            }},
            "Intent": "verificar_status"
        }}

        Lembre-se de identificar corretamente as entidades e a intenção conforme o conteúdo da entrada.
        """

    def get_response_html(self, user_input: str) -> str:
        try:
            prompt = self._build_prompt(user_input)
            response = self.chat_session.send_message(prompt)
            html_response = markdown.markdown(response.text)
            return html_response
        except GoogleAPIError as e:
            return f"[Erro Gemini API] Código: {e.code if hasattr(e, 'code') else 'desconhecido'} - {str(e)}"
        except Exception as e:
            return f"[Erro inesperado] {str(e)}"

    def get_response_json(self, user_input: str) -> dict:
        prompt = self._build_prompt(user_input)
        try:
            response = self.chat_session.send_message(prompt)
            content = response.text.strip()
            match = re.search(r"```json\s*(\{.*?\})\s*```", content, re.DOTALL)
            if match:
                json_block = match.group(1)
                try:
                    # print(content)
                    return json.loads(json_block)
                except json.JSONDecodeError:
                    return {
                        "Erro": "Não foi possível interpretar o JSON retornado pela API.",
                        "Resposta": json_block
                    }
            
        
            return {
                        "Erro": "Bloco JSON não encontrado na resposta da API.",
                        "Resposta": content
                    }

        except GoogleAPIError as e:
            return {
                "Erro": f"[Erro Gemini API] Código: {e.code if hasattr(e, 'code') else 'desconhecido'} - {str(e)}"
            }
        except Exception as e:
            return {
                "Erro": f"[Erro inesperado] {str(e)}"
            }