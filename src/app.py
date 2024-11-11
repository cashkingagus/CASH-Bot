from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response = process_message(user_message)
    return jsonify({'response': response})

def process_message(message):
    # Basic response for now (you can later replace this with AI logic)
    if "hello" in message.lower():
        return "Hi! How can I assist you today?"
    else:
        return "I'm sorry, I didn't understand that."

if __name__ == '__main__':
    app.run(debug=True)