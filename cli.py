# cogni_scaffold/cli.py
from .server import mcp

def main():
    """
    Command-line entry point to run the CogniScaffold MCP server.
    """
    print("Starting CogniScaffold MCP server on http://127.0.0.1:8080")
    mcp.run(transport="http", host="127.0.0.1", port=8080)
