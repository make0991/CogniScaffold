# cogni_scaffold/server.py

import json
import time
from flask import Flask, request, Response, stream_with_context
from . import CogniScaffold

# Initialize the Flask app and the CogniScaffold tool
app = Flask(__name__)
scaffold = CogniScaffold()

def sse_format(data_dict: dict) -> str:
    """Formats a dictionary into a Server-Sent Event string."""
    return f"data: {json.dumps(data_dict)}\n\n"

@app.route('/search')
def search_endpoint():
    """
    Endpoint to search for frameworks.
    Streams results one by one.
    Usage: /search?q=<keyword>
    """
    keyword = request.args.get('q', '')
    if not keyword:
        return Response(
            sse_format({"error": "Query parameter 'q' is required."}),
            mimetype='text/event-stream'
        )

    def generate():
        try:
            results = scaffold.search(keyword)
            if not results:
                yield sse_format({"message": "No frameworks found."})
            else:
                for result in results:
                    yield sse_format(result)
                    time.sleep(0.1) # Simulate work
            yield sse_format({"event": "done"})
        except Exception as e:
            yield sse_format({"error": str(e)})

    return Response(stream_with_context(generate()), mimetype='text/event-stream')

@app.route('/template/<framework_name>')
def template_endpoint(framework_name):
    """
    Endpoint to get a framework template.
    Streams the result as a single event.
    Usage: /template/swot
    """
    def generate():
        try:
            template_md = scaffold.get_template(framework_name)
            if "Error:" in template_md:
                yield sse_format({"error": template_md})
            else:
                yield sse_format({"name": framework_name, "template": template_md})
            yield sse_format({"event": "done"})
        except Exception as e:
            yield sse_format({"error": str(e)})
            
    return Response(stream_with_context(generate()), mimetype='text/event-stream')

@app.route('/suggest', methods=['POST'])
def suggest_endpoint():
    """
    Endpoint to suggest frameworks for a problem description.
    Streams results one by one.
    Usage: POST /suggest with JSON body: {"problem": "description..."}
    """
    if not request.json or 'problem' not in request.json:
        return Response(
            sse_format({"error": "JSON body with 'problem' key is required."}),
            mimetype='text/event-stream'
        )
    
    problem = request.json['problem']

    def generate():
        try:
            suggestions = scaffold.suggest(problem)
            if not suggestions:
                yield sse_format({"message": "Could not find any relevant frameworks."})
            else:
                for suggestion in suggestions:
                    yield sse_format(suggestion)
                    time.sleep(0.1) # Simulate work
            yield sse_format({"event": "done"})
        except Exception as e:
            yield sse_format({"error": str(e)})

    return Response(stream_with_context(generate()), mimetype='text/event-stream')

if __name__ == '__main__':
    # To run this server:
    # 1. Make sure you are in the parent directory (e.g., 'playground').
    # 2. Run the command:
    #    ./cogni_scaffold/.venv/bin/flask --app cogni_scaffold.server:app run
    print("This file is not meant to be run directly. Use Flask CLI.")
    print("Example: ./cogni_scaffold/.venv/bin/flask --app cogni_scaffold.server:app run")
