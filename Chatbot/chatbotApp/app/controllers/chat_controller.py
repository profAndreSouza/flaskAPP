from flask import request, render_template
from app.services.chatbot_service import get_bot_response

def chatbot():
    user_input = ""
    bot_response = ""
    if request.method == "POST":
        user_input = request.form.get("message")
        bot_response = get_bot_response(user_input)
    return render_template("index.html", user_input=user_input, 
                           bot_response=bot_response)
