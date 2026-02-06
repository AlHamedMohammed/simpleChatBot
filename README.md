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
