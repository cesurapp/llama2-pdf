from flask import Flask, Response, request, jsonify
from flask_cors import CORS
from waitress import serve
from dotenv import load_dotenv
import os
from ai import AI
from utils import Utils

load_dotenv()
app = Flask(__name__)
cors = CORS(app, origins=['*'])
ai = AI()

@app.before_request
def handle_preflight():
    if request.method == "OPTIONS":
        res = Response()
        res.headers['X-Content-Type-Options'] = '*'
        return res

# Home Page
@app.route('/', methods=['GET'])
def homepage():
    return jsonify('Meta LLamaCpp Port AI Server')

@app.route('/ask', methods=['POST'])
def ask():
    jsonBody = request.json
    
    # Text Context
    if "textContext" in jsonBody:
        return jsonify({"answers": ai.askText(jsonBody['textContext'], jsonBody['prompts'])})
    
    # PDF Context
    if "pdfContextBase64" in jsonBody:
        return jsonify({"answers": ai.askText(Utils.base64PdfToText(jsonBody['pdfContextBase64']), jsonBody['prompts'])})

    # Chat
    return jsonify({"answers": ai.askAi(jsonBody['prompts'])})

# Run Flask App
if __name__ =='__main__':
    serve(app, host=os.getenv('HOST'), port=os.getenv('PORT'))