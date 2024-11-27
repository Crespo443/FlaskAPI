from flask import Flask, request, jsonify
from controller import process_text

app = Flask(__name__)

@app.route('/api/process', methods=['POST'])
def process_text_route():
    return process_text()