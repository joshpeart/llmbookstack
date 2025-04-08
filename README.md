# LLM + Bookstack

This project is a Flask-based web application that uses AI (ChatGPT or Ollama) to generate structured, Markdown-formatted knowledgebase content — which can be reviewed, edited, and pushed directly into your [BookStack](https://www.bookstackapp.com/) instance.

## ✨ Features

- Generate documentation from a simple topic prompt using ChatGPT or Ollama.
- Automatically creates chapters and pages with Markdown content.
- Live preview and in-browser editing of generated content.
- Drag-and-drop reordering of chapters and pages.
- Push content directly into BookStack via its API.
- Toggle between ChatGPT (OpenAI) or local Ollama models (LLaMA 3.2 / Code LLaMA).

## 📸 Screenshot

![screenshot]![image](https://github.com/user-attachments/assets/c3b4df90-7e34-4e49-b465-351dbae3fb8a)

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
