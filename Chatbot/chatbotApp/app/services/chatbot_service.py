import os
from dotenv import load_dotenv
import google.generativeai as genai
from google.api_core.exceptions import GoogleAPIError

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-pro")
chat_session = model.start_chat(history=[])

def get_bot_response(user_input: str) -> str:
    try:
        response = chat_session.send_message(user_input)
        return response.text
    except GoogleAPIError as e:
        return f"[Erro Gemini API] Código: {e.code if hasattr(e, 'code') else 'desconhecido'} - {str(e)}"
    except Exception as e:
        return f"[Erro inesperado] {str(e)}"
