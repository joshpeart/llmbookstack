# app/bookstack_api.py

import os
import requests
from dotenv import load_dotenv

load_dotenv()

BOOKSTACK_URL = os.getenv("BOOKSTACK_URL")
TOKEN_ID = os.getenv("BOOKSTACK_TOKEN_ID")
TOKEN_SECRET = os.getenv("BOOKSTACK_TOKEN_SECRET")

HEADERS = {
    "Authorization": f"Token {TOKEN_ID}:{TOKEN_SECRET}",
    "Content-Type": "application/json"
}

def create_book(title):
    res = requests.post(f"{BOOKSTACK_URL}/api/books", json={"name": title}, headers=HEADERS)
    res.raise_for_status()
    return res.json().get("id")

def create_chapter(book_id, title):
    res = requests.post(f"{BOOKSTACK_URL}/api/chapters", json={"book_id": book_id, "name": title}, headers=HEADERS)
    res.raise_for_status()
    return res.json().get("id")

def create_page(book_id, chapter_id, title, content):
    res = requests.post(f"{BOOKSTACK_URL}/api/pages", json={
        "book_id": book_id,
        "chapter_id": chapter_id,
        "name": title,
        "markdown": content
    }, headers=HEADERS)
    return res.status_code == 200

def push_to_bookstack(kb_data):
    book_id = create_book("AI-Generated Knowledgebase")
    for chapter_title, pages in kb_data.items():
        chapter_id = create_chapter(book_id, chapter_title)
        for page_title, content in pages.items():
            create_page(book_id, chapter_id, page_title, content)
    return {"success": True}
