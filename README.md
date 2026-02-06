# simpleChatBot

# ChatBot – AI-Powered Conversational Interface

## 📌 Project Overview
This project is a **Next-Gen AI ChatBot** built with **Python (Flask)** for the backend and **HTML, CSS, JavaScript** for the frontend. It demonstrates a clean separation of concerns, modern frontend design, and integration with **OpenRouter API** for AI-powered responses.  

Users can interact with an AI assistant in real-time, simulating a professional conversational interface suitable for customer support or virtual assistance.

---

## 🛠 Features
- **Real-time AI responses** using OpenRouter API (GPT-4 models)  
- **Frontend–Backend Separation**:
  - Python handles backend logic and API calls  
  - HTML handles structure, CSS handles style, JS handles interactions  
- **Typing indicator & chat animations** for realistic conversations  
- **Secure API key storage** using `.env`  
- **Responsive design** for mobile and desktop devices  
- **Scalable architecture** for chat history, multi-user support, or multiple AI models  

---

## ⚙️ Technology Stack
- **Backend**: Python 3.12+, Flask, Requests, python-dotenv  
- **Frontend**: HTML5, CSS3, JavaScript (AJAX + DOM manipulation)  
- **AI Integration**: OpenRouter API  
- **Environment Management**: `.env` for API keys  

---

## 🚀 How It Works
1. User sends a message via the chat input.  
2. JavaScript sends the message to Flask backend via `/api/chat`.  
3. Flask backend calls OpenRouter API using the secure API key.  
4. AI response is returned and displayed in the frontend chat interface.  
5. Messages show timestamps and typing animations.  

---

## 📁 Project Structure

chatBot/
├── app.py # Flask backend logic
├── .env # Secure API key
├── templates/
│ ├── base.html # Base HTML template
│ └── index.html # Main chat page
├── static/
│ ├── css/
│ │ └── style.css # Styling
│ └── js/
│ └── script.js # Frontend logic
└── requirements.txt # Python dependencies


---

## ⚡ Quick Overview for HR
- **Backend:** Python + Flask handles chat logic and API calls  
- **Frontend:** HTML/CSS/JS for interactive chat UI with animations  
- **AI Integration:** OpenRouter API for smart AI responses  
- **Security:** API key stored in `.env`, never exposed to frontend  
- **Responsive & Scalable:** Works on mobile and desktop, designed for easy expansion  

---

## 🚀 How It Works
1. User types a message in the frontend input box.  
2. JavaScript sends the message to the Flask backend (`/api/chat`).  
3. Flask calls OpenRouter API using the secure API key.  
4. AI response is returned and displayed in the chat interface with timestamps and typing animations.  

---

## 💡 Skills Demonstrated
- Full-stack web development  
- Secure API integration  
- Frontend animations & responsive UI  
- AJAX-based real-time communication  
- Environment management using `.env` files  

---


---

## ⚡ Quick Start

1. Clone the repository:

```bash
git clone <repo-url>
cd chatBot

2. Install dependencies:
  python -m pip install -r requirements.txt

3. Create a .env file with your OpenRouter API key:
  OPENROUTER_API_KEY=sk-or-v1-xxxxxxxxxxxxxxxx

4. Run the Flask server:
  python app.py

5. Open your browser at:
  http://127.0.0.1:5000
