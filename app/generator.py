# app/generator.py

import os
import requests
import openai
from dotenv import load_dotenv
import json
import base64
import zlib

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://192.168.0.48:11434")

def query_ollama(prompt, model="llama3.2"):
    response = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={"model": model, "prompt": prompt, "stream": False},
    )
    response.raise_for_status()
    return response.json().get("response", "")

def generate_knowledgebase(topic, provider):
    def send(msg):
        yield f"data: {msg}\n\n"

    yield from send(f"⏳ Generating outline for '{topic}'...")

    outline_prompt = f"Generate a Markdown-formatted knowledge base outline for the topic: {topic}"

    if provider == "ollama":
        outline_text = query_ollama(outline_prompt, model="llama3.2")
    else:
        chat_response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful technical documentation writer."},
                {"role": "user", "content": outline_prompt},
            ]
        )
        outline_text = chat_response.choices[0].message.content

    chapters = {}
    current_chapter = None
    for line in outline_text.strip().split("\n"):
        line = line.strip()
        if not line:
            continue
        if line.startswith("#"):
            current_chapter = line.strip("# ").strip()
            chapters[current_chapter] = []
        elif (line.startswith("-") or line.startswith("*")) and current_chapter:
            chapters[current_chapter].append(line.strip("-* ").strip())

    final_content = {}
    total_pages = sum(len(pages) for pages in chapters.values())
    completed = 0

    for chapter, pages in chapters.items():
        yield from send(f"📂 Creating chapter: {chapter}")
        final_content[chapter] = {}
        for page in pages:
            yield from send(f"📝 Generating page: {page} under {chapter}")
            page_prompt = f"Write a detailed, markdown-formatted knowledge base article for the topic: '{page}' under the chapter '{chapter}'. Include headings, bullet points, and code examples where appropriate."

            if provider == "ollama":
                model = "codellama" if "code" in page.lower() or "example" in page.lower() else "llama3.2"
                article = query_ollama(page_prompt, model=model)
            else:
                chat_response = openai.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "You are a helpful technical documentation writer."},
                        {"role": "user", "content": page_prompt},
                    ]
                )
                article = chat_response.choices[0].message.content

            final_content[chapter][page] = article
            completed += 1
            percent = int((completed / total_pages) * 100)
            yield from send(f"__PROGRESS__ {percent}")

    yield from send("✅ All content generated, preparing for final output...")

    # Compress and encode the full result
    compressed = zlib.compress(json.dumps(final_content).encode("utf-8"))
    encoded = base64.b64encode(compressed).decode("utf-8")

    yield f"data: __JSON_B64__ {encoded}\n\n"
    yield f"data: __COMPLETE__\n\n"
