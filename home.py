import google.generativeai as cbert
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from utility.readability import analyze_code

app = Flask(__name__)
CORS(app)
api_key = "AIzaSyBEMcs_QdejjbBQkOpWQjEPy2IWCm63No0"
cbert.configure(api_key=api_key)


@app.route("/", methods=["POST"])
def prompt():
    data = request.json
    prompt = data.get("prompt", "")
    content = data.get("content", "")

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    try:
        model = cbert.GenerativeModel("gemini-pro")

        response = model.generate_content(prompt + " : " + content)

        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": "Request failed"}), 500


@app.route("/readability", methods=["POST"])
def readabable():
    data = request.json
    content = data.get("content", "")

    return analyze_code(content)


app.run(debug=True)
