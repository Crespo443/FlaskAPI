from flask import request, jsonify
from service import process_text_service

def process_text():
    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({"error": "Text input is required."}), 400
    
    text = data["text"]
    if type(text) != str:
        return jsonify({
            "error" : "Text value should be string"
        }), 400
    try:
        processed_data = process_text_service(text)
        return jsonify(processed_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
