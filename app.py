from flask import Flask, jsonify, render_template, request
import wikipedia

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# ✅ safer API (no URL issues)
@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    query = data.get("query", "")

    try:
        result = wikipedia.summary(query, sentences=2)
    except Exception as e:
        print("ERROR:", e)
        result = "Sorry, I couldn't find information."

    return jsonify({"response": result})