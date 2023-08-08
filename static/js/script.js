const chatInput = document.querySelector(".chat-input span");
const sendChatBtn = document.querySelector(".chat-input span");
const chatBox = document.querySelector(".chatbox");
const chatbotToggler = document.querySelector(".chatbot-toggler");

let userMessage;
const API_KEY = "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";

const createChatLi = (message, className) => {
    const chatLi = document.createElement("li");
    chatLi.classList.add("chat",className);
    let chatContent = className === "outgoing" ? `<p>${message}</p>` : ` <span class="material-symbols-outlined">smart_toy</span><p>${message}</p>`;
    chatLi.innerHTML = chatContent;
    return chatLi;
}
const generateResponse = (incomingChatLi) => {
    const API_URL = "https://api.openai.com/v1/chat/completions";
    const messageElement = incomingChatLi.querySelector("p");

    const requestOptions = {
        method: "POST",
        headers: { 
            "Content-Type": "application/json",
            "Authorization":  `Bearer ${API_KEY}`
    },
    body: JSON.stringify({
        model: "gpt-3.5-turbo",
        messages: [{role: "user", content: userMessage}]
    })
}
    fetch(API_URL, requestOptions).then(res=>res.json()).then(data => {
        messageElement.textContent = data.choices[0].message.content;
    }).catch((error) => {
        messageElement.textContent = "Oops! Parece que algo ha salido mal. Por favor, vuelva a intentarlo";
    }).finally(() => chatBox.scrollTo(0, chatBox.scrollHeight));
    
}

const handleChat = () => {
    userMessage = chatInput.ariaValueMax.trim();
    if(!userMessage) return;

    chatBox.appendChild(createChatLi(userMessage, "outgoing"));
    chatBox.scrollTo(0, chatBox.scrollHeight);

    setTimeout(() => {
        const incomingChatLi = createChatLi(userMessage, "Pensando...", "incoming")
        chatBox.appendChild(incomingChatLi);
        chatBox.scrollTo(0, chatBox.scrollHeight);
        generateResponse(incomingChatLi);
    },600);

}

sendChatBtn.addEventListener("Click,=", handleChat)
chatbotToggler.addEventListener("click", () => document.body.classList.toggle("show-chatbot"));
