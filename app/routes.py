# app/routes.py

from flask import Blueprint, request, render_template, jsonify, stream_with_context, Response
from .generator import generate_knowledgebase
from .bookstack_api import push_to_bookstack

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/generate', methods=['POST'])
def generate():
    topic = request.json.get('topic')
    provider = request.json.get('provider')

    def event_stream():
        try:
            for message in generate_knowledgebase(topic, provider):
                yield message
        except Exception as e:
            yield f"data: __ERROR__ {str(e)}\n\n"

    return Response(stream_with_context(event_stream()), mimetype="text/event-stream")

@main.route('/push', methods=['POST'])
def push():
    kb_data = request.json.get('kb_data')
    result = push_to_bookstack(kb_data)
    return jsonify(result)
