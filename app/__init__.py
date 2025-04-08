import os
from flask import Flask
from .routes import main

def create_app():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    templates_path = os.path.join(base_dir, "templates")

    print("🔍 Template folder resolved as:", templates_path)

    app = Flask(__name__, template_folder=templates_path)
    app.secret_key = os.getenv("FLASK_SECRET_KEY", "fallback_key")
    app.register_blueprint(main)

    return app


