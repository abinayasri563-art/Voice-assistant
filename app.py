from flask import Flask, jsonify
import wikipedia

app = Flask(__name__)

@app.route("/")
def home():
    return "App is running!"

@app.route("/wiki/<query>")
def wiki(query):
    result = wikipedia.summary(query, sentences=2)
    return jsonify({"result": result})