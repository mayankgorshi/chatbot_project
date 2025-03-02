from flask import Flask, request, jsonify
from fuzzywuzzy import process  # Import fuzzy matching

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chatbot():
    user_input = request.json.get("message", "").lower()  

    responses = {
        "hi": "Hello! How can I help you?",
        "how are you": "I'm just a bot, but I'm doing great!",
        "bye": "Goodbye! Have a nice day!"
    }

    # Find the closest match
    best_match, score = process.extractOne(user_input, responses.keys())

    # If similarity score is high, return matched response, else default
    if score > 60:  # Threshold for similarity
        reply = responses[best_match]
    else:
        reply = "I'm not sure how to respond to that."

    return jsonify({"response": reply})

if __name__ == '__main__':
    app.run(debug=True)
