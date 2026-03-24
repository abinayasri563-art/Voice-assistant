from flask import Flask, jsonify, render_template
import wikipedia

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask/<query>")
def ask(query):
    try:
        result = wikipedia.summary(query, sentences=2)
    except:
        result = "Sorry, I didn't understand"
    return jsonify({"response": result})