from flask import Flask, jsonify, render_template
import wikipedia

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask/<path:query>")   # ✅ FIXED (path allows spaces)
def ask(query):
    try:
        result = wikipedia.summary(query, sentences=2)
    except Exception as e:
        print("ERROR:", e)   # shows in logs
        result = "Sorry, I couldn't find information."

    return jsonify({"response": result})