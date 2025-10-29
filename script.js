async function sendMessage() {
  const input = document.getElementById("user-input");
  const message = input.value;
  if (!message) return;

  const chatBox = document.getElementById("chat-box");
  chatBox.innerHTML += `<div class="message user">You: ${message}</div>`;
  input.value = "";

  // Send the message to Flask backend
  const response = await fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message })
  });

  const data = await response.json();
  chatBox.innerHTML += `<div class="message bot">Bot: ${data.reply}</div>`;
  chatBox.scrollTop = chatBox.scrollHeight;
}

document.querySelector("button").addEventListener("click", sendMessage);