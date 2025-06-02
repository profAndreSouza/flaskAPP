from flask import request, jsonify

def query():
    try:
        data = request.get_json()

        action = data.get("action")
        entities = data.get("entities")

        if not action or not entities:
            return jsonify({"error": "Parâmetros 'action' e 'entities' são obrigatórios."}), 400

        return jsonify({
            "message": "Requisição processada com sucesso.",
            "action": action,
            "entities": entities
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
