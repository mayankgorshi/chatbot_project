from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, your chatbot is live!"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get("message", "")
    return jsonify({"response": f"you said: {message}"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

