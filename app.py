@app.route("/ask/<query>")
def ask(query):
    try:
        result = wikipedia.summary(query, sentences=2)
    except Exception as e:
        result = "Sorry, I couldn't find information."

    return jsonify({"response": result})