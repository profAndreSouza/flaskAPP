from .app import create_app

app = create_app()

@app.route('/')
def index():
    return "Chatbot funcionando!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
