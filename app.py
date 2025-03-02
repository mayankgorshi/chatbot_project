from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chatbot():
    user_input = request.json.get("message")

    responses = {
        "hi": "hello! How can i help you?",
        "how are you": "I'm just a bot, but I'm doing great!",
        "bye": "Goodbye! Have a nice day!"
    }

    response = responses.get(user_input.lower(), "Sorry, I don't understand that.")
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True) 
