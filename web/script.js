async function sendMessage() {
  const input = document.getElementById("user-input");
  const message = input.value.trim();
  if (!message) return;

  appendMessage(message, "user");
  input.value = "";

  const typing = appendTyping();

  try {
    const res = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message })
    });

    const data = await res.json();
    typing.remove();
    appendMessage(data.response, "bot");

  } catch (err) {
    typing.remove();
    appendMessage("⚠️ Something went wrong. Please try again.", "bot");
  }
}

function appendMessage(text, sender) {
  const chatBox = document.getElementById("chat-box");
  const div = document.createElement("div");
  div.className = sender === "user" ? "user-message" : "bot-message";
  div.innerText = text;
  chatBox.appendChild(div);
  chatBox.scrollTop = chatBox.scrollHeight;
}

function appendTyping() {
  const chatBox = document.getElementById("chat-box");
  const div = document.createElement("div");
  div.className = "bot-message";
  div.innerText = "Typing...";
  chatBox.appendChild(div);
  chatBox.scrollTop = chatBox.scrollHeight;
  return div;
}
