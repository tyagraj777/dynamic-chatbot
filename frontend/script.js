async function sendMessage() {
    const userInput = document.getElementById("userInput").value;
    const response = await fetch("/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({message: userInput})
    });
    const data = await response.json();
    document.getElementById("messages").innerHTML += `<p>You: ${userInput}</p>`;
    document.getElementById("messages").innerHTML += `<p>Bot: ${data.response}</p>`;
}
