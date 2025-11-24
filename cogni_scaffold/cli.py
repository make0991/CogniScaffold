# cogni_scaffold/cli.py
import argparse
from .server import mcp

def main():
    """
    Command-line entry point to run the CogniScaffold MCP server.
    """
    parser = argparse.ArgumentParser(description="Run the CogniScaffold MCP server.")
    parser.add_argument("--port", type=int, default=8080, help="Port to run the server on.")
    args = parser.parse_args()

    print(f"Starting CogniScaffold MCP server on http://127.0.0.1:{args.port}")
    mcp.run(transport="http", host="127.0.0.1", port=args.port)
