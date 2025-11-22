# CogniScaffold

**CogniScaffold** is a Python tool designed to act as a "cognitive scaffold" for structured thinking and analysis. It provides a curated knowledge base of analytical frameworks and an API to search, template, and get suggestions for applying them.

## Core Philosophy

In today's world, the challenge is often not the lack of information, but the lack of structure to process it. This tool is built on the cognitive science concept of "Cognitive Scaffolding" — providing temporary, structured support to help users tackle complex analytical tasks that might otherwise be overwhelming.

It is designed not to replace human thinking, but to augment and enhance it. It helps you answer the question, "How should I think about this problem?"

## Features

`CogniScaffold` provides three core functionalities:

1.  **Search (`.search(keyword)`)**: Find relevant analytical frameworks from the knowledge base.
2.  **Get Template (`.get_template(name)`)**: Generate a clean, structured Markdown template for a specific framework, ready to be filled in.
3.  **Suggest (`.suggest(problem_description)`)**: Get recommendations for which frameworks to apply to a given problem.

## The Knowledge Base

The core of `CogniScaffold` is a manually curated Python dictionary of powerful mental models and frameworks, including:

-   SWOT Analysis
-   Porter's Five Forces
-   PESTLE Analysis
-   BCG Matrix
-   Pyramid Principle
-   First Principles Thinking
-   And more...

## Getting Started

To use the tool, import the `CogniScaffold` class and create an instance:

```python
from cogni_scaffold import CogniScaffold

# Create an instance of the tool
scaffold = CogniScaffold()

# Now you can use its methods
...
```

See `main.py` for a detailed usage example as a library.

## Running as a Server

CogniScaffold can also be run as a streaming HTTP server using Flask.

### 1. Setup

First, create and activate a virtual environment, then install the dependencies:

```bash
# From the project root directory
python3 -m venv .venv
# Install dependencies into the virtual environment
./.venv/bin/pip install -r requirements.txt
```

### 2. Execution

Run the server using the Flask CLI. Make sure you are in the parent directory of `cogni_scaffold`.

```bash
./.venv/bin/flask --app cogni_scaffold.server:app run
```

The server will start, typically on `http://127.0.0.1:5000`.

## API Endpoints

All endpoints provide responses in a streaming `text/event-stream` format.

### `GET /search?q=<keyword>`

Searches for frameworks. Each matching framework is sent as a separate JSON object in the stream.

**Example:** `curl http://127.0.0.1:5000/search?q=competition`

### `GET /template/<framework_name>`

Retrieves the Markdown template for a specific framework.

**Example:** `curl http://127.0.0.1:5000/template/swot`

### `POST /suggest`

Suggests frameworks based on a JSON payload. Each suggestion is sent as a separate event in the stream.

**Example:**
```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"problem": "We need to analyze our market position."}' \
http://127.0.0.1:5000/suggest
```

## Future Development

This prototype can be expanded by:
-   Continuously growing the framework knowledge base.
-   Improving the `suggest()` method with more sophisticated NLP techniques.
-   Adding a command-line interface (CLI) for quick access.
