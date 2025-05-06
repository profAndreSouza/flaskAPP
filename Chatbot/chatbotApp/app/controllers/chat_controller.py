from flask import request, render_template, session, redirect, url_for
from app.services.gemini_service import GeminiService

gemini_service = GeminiService()

def chatbot():
    if "chat_history" not in session:
        session["chat_history"] = []

    if request.method == "POST":
        user_input = request.form.get("message")
        if user_input:
            bot_response = gemini_service.get_response_html(user_input)
            
            session["chat_history"].append({"user": user_input, "bot": bot_response})
            session.modified = True

        return redirect(url_for("chatbot.chatbot"))

    return render_template("index.html", chat_history=session["chat_history"])
