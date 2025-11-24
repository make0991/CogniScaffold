# cogni_scaffold/server.py
from .core import CogniScaffold
from fastmcp import FastMCP

mcp = FastMCP(
    name="CogniScaffold",
)

# Create a single, shared instance of the tool
cogni_scaffold_instance = CogniScaffold()

@mcp.tool
def search(keyword: str) -> list[dict]:
    """
    Searches for thinking frameworks by keyword.
    """
    return cogni_scaffold_instance.search(keyword)

@mcp.tool
def get_template(name: str) -> str:
    """
    Gets the markdown template for a specific thinking framework.
    """
    return cogni_scaffold_instance.get_template(name)

@mcp.tool
def suggest(problem_description: str) -> list[dict]:
    """
    Suggests relevant thinking frameworks for a given problem description.
    """
    return cogni_scaffold_instance.suggest(problem_description)
