# from flask import Flask, render_template, jsonify, request # type: ignore
# import random

# app = Flask(__name__)

# BOT_RESPONSES = [
#     "That's an interesting question! Let me help you with that.",
#     "I understand. Here's what I think about that topic.",
#     "Great point! I can assist you with more information.",
#     "Thanks for sharing! I'm here to help you navigate this.",
#     "I see what you mean. Let me provide some insights on that.",
#     "Excellent question! Let's explore this together.",
#     "I appreciate your message. Here's my take on it.",
#     "That's a thoughtful query. I'd be happy to assist."
# ]

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/api/chat", methods=["POST"])
# def chat():
#     user_message = request.json.get("message", "")
#     response = random.choice(BOT_RESPONSES)
#     return jsonify({"reply": response})

# if __name__ == "__main__":
#     app.run(debug=True)
from flask import Flask, render_template, jsonify, request
import requests
import os
from dotenv import load_dotenv  # <-- import here

# ------------------------------
# Load environment variables from .env
load_dotenv()  # <-- load .env file
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")  # <-- read your API key
# print(OPENROUTER_API_KEY)  # optional: test that it works
# ------------------------------

app = Flask(__name__)

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost:5000",
    "X-Title": "Flask ChatBot"
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    payload = {
        "model": "openai/gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": user_message}
        ]
    }

    response = requests.post(OPENROUTER_URL, headers=HEADERS, json=payload, timeout=30)

    if response.status_code != 200:
        return jsonify({"reply": "⚠️ AI service error. Try again."}), 500

    data = response.json()
    ai_reply = data["choices"][0]["message"]["content"]

    return jsonify({"reply": ai_reply})

if __name__ == "__main__":
    app.run(debug=True)
