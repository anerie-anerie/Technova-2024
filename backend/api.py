from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key here (or via environment variables)
openai.api_key = 'your-openai-api-key'

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    chat_history = data.get('chat_history', [])

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    # Call OpenAI API with the same logic from your Streamlit app
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_history + [{"role": "user", "content": user_message}]
    )

    assistant_reply = response['choices'][0]['message']['content']

    # Append the new assistant message to chat history and return it
    updated_chat_history = chat_history + [
        {"role": "user", "content": user_message},
        {"role": "assistant", "content": assistant_reply}
    ]

    return jsonify({
        "assistant_reply": assistant_reply,
        "chat_history": updated_chat_history
    })

if __name__ == '__main__':
    app.run(debug=True)
