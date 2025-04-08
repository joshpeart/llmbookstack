# LLM + Bookstack

This project is a Flask-based web application that uses AI (ChatGPT or Ollama) to generate structured, Markdown-formatted knowledgebase content — which can be reviewed, edited, and pushed directly into your [BookStack](https://www.bookstackapp.com/) instance.

## ✨ Features

- 🔍 Input a topic and select an AI model provider (ChatGPT or Ollama)
- ⚙️ Streamed AI-powered content generation (uses OpenAI GPT-4 or Ollama Llama 3.2/Code LLaMA)
- 📝 Editable chapters and pages with live Markdown preview
- 📂 Drag-and-drop reordering of sections and content
- 📤 Push final content to your BookStack documentation portal
- 🌐 Built using Flask + vanilla JS (no heavy frontend frameworks)

## 📸 Screenshot

[screenshot]![image](https://github.com/user-attachments/assets/c3b4df90-7e34-4e49-b465-351dbae3fb8a)
[screenshot]![image](https://github.com/user-attachments/assets/ac221a66-e8b4-4df5-a0de-64cdacbef671)
Bookstack Output

## 🚀 Requirements

- Python 3.8+
- Flask
- OpenAI account and API key (for ChatGPT usage)
- [Ollama](https://ollama.com/) installed and running locally (for local LLM usage)
- A running instance of [BookStack](https://www.bookstackapp.com/)

## 🧰 Dependencies

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Environment variables are stored in a .env file in the root directory of the project:

```bash
OPENAI_API_KEY=your-openai-api-key
OLLAMA_URL=http://localhost:11434
BOOKSTACK_URL=http://your-bookstack-url
BOOKSTACK_TOKEN_ID=your-token-id
BOOKSTACK_TOKEN_SECRET=your-token-secret
```

## 📚 Installing BookStack
Full install instructions can be found here:
👉 https://www.bookstackapp.com/docs/admin/installation/

We recommend using the Docker installation method if you're not familiar with Laravel/PHP-based setups.

## 🛠️ Running the App
```bash
docker compose up --build
```
Then visit http://localhost:5000 in your browser.

## 💡 Example Use Cases
Technical documentation for software products

Internal knowledgebase generation for teams

Automatically drafting wiki content

Educational or training material

## 🧠 AI Model Behavior
Uses llama3.2 by default when using Ollama.

Automatically switches to Code LLaMA for topics that include "code" or "example".

With ChatGPT, uses GPT-4 and custom system prompts to generate clean, helpful Markdown.

## 🧪 Development Tips
Streamed responses use Server-Sent Events (SSE) for live updates in the UI.

Markdown rendering is done with marked.js.

Compression and base64 encoding are used to safely transmit large generated content blocks.

## 🤝 Contributing
Pull requests are welcome! If you have improvements, ideas, or find a bug — feel free to open an issue or submit a PR.

## 📄 License
MIT

Built with ❤️ by Josh Peart and ChatGPT
Inspired by the dream of effortless, structured documentation.

