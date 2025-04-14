from flask import request, render_template

def chatbot():
    user_input = ""
    bot_response = ""
    if request.method == "POST":
        user_input = request.form.get("message")
        bot_response = "resposta"
    return render_template("index.html", user_input=user_input, 
                           bot_response=bot_response)
