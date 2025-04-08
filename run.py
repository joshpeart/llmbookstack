# run.py

import os
from flask import Flask
from app.routes import main
from dotenv import load_dotenv

load_dotenv()

def create_app():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    template_path = os.path.join(base_dir, "app", "templates")  # 👈 Explicit path

    app = Flask(__name__, template_folder=template_path)
    app.secret_key = os.getenv("FLASK_SECRET_KEY", "fallback_key")
    app.register_blueprint(main)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)