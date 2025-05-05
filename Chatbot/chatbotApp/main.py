from app import create_app
from app.nlp.text_processor import TextPreProcessor
from app.nlp.syntatic_analyzer import SyntaticAnalyzer
from app.nlp.semantic_analyzer import SemanticAnalyzer

app = create_app()

@app.route('/')
def index():
    perguntas_classificacao = [
        "Quantas peças de cada tipo (metálicas, plásticas, refugos) são processadas por hora e qual é a taxa média de acerto da classificação?",
        "Quais são as etapas envolvidas no processo de classificação, desde a entrada da peça até sua separação final?",
        "Como o sistema identifica e diferencia materiais metálicos, plásticos e refugos? (Ex: sensores, visão computacional, inteligência artificial?)",
        "Existe algum controle de qualidade ou verificação humana posterior à classificação automática para evitar erros?",
        "Qual é a taxa de refugo do sistema — ou seja, quantas peças são classificadas como refugo por engano ou por não atenderem aos critérios definidos?"
    ]

    resposta = []
    for enunciado in perguntas_classificacao:

        preprocessor = TextPreProcessor()
        preprocessado = preprocessor.preprocess(enunciado)
        
        syntatic = SyntaticAnalyzer()
        sintaxe = syntatic.analyze(preprocessado)

        semantic = SemanticAnalyzer()
        entity, intent = semantic.extract_intent_and_intentions(enunciado)

        resposta.append({
            "Original": enunciado,
            "Pré-processado": preprocessado ,
            "Entidades": entity,
            "Intenção": intent
        })
    
    return resposta

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
