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

## Installation and Usage

`CogniScaffold` is packaged as a standard Python library and can be installed using `pip`. It is recommended to install it within a virtual environment.

### 1. Installation

From the project root directory, run the following command to install the package in editable mode:

```bash
pip install -e .
```

This will install `cogni_scaffold` and its dependencies, including the `FastMCP` server.

### 2. Running the MCP Server

Once installed, you can run the `CogniScaffold` MCP server using the command-line entry point:

```bash
cogni-scaffold
```

Alternatively, you can run it as a module:

```bash
python -m cogni_scaffold
```

The server will start and be available for MCP clients to connect to.

## Future Development

This prototype can be expanded by:
-   Continuously growing the framework knowledge base.
-   Improving the `suggest()` method with more sophisticated NLP techniques.
-   Adding more tools and resources to the MCP server.

