const messagesContainer = document.getElementById("messages");
const messageInput = document.getElementById("messageInput");
const sendButton = document.getElementById("sendButton");
const typingIndicator = document.getElementById("typingIndicator");

function getTimestamp() {
    const now = new Date();
    return now.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
}

function addMessage(text, isUser) {
    const messageDiv = document.createElement("div");
    messageDiv.className = `message ${isUser ? "user" : "bot"}`;

    messageDiv.innerHTML = `
        <div class="avatar">${isUser ? "U" : "AI"}</div>
        <div class="message-content">
            <div class="message-bubble">
                ${text}
                <div class="timestamp">${getTimestamp()}</div>
            </div>
        </div>
    `;

    messagesContainer.appendChild(messageDiv);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

function showTyping() {
    typingIndicator.classList.add("active");
}

function hideTyping() {
    typingIndicator.classList.remove("active");
}

async function sendMessage() {
    const text = messageInput.value.trim();
    if (!text) return;

    addMessage(text, true);
    messageInput.value = "";

    showTyping();

    const response = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: text })
    });

    const data = await response.json();
    hideTyping();
    addMessage(data.reply, false);
}

sendButton.addEventListener("click", sendMessage);
messageInput.addEventListener("keypress", e => {
    if (e.key === "Enter") sendMessage();
});
