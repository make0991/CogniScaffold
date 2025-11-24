# cogni_scaffold/server.py
from .cogni_scaffold import CogniScaffold
from fastmcp import FastMCP

mcp = FastMCP(
    name="CogniScaffold",
)

cogni_scaffold = CogniScaffold()

@mcp.tool
def search(keyword: str) -> list[dict]:
    """
    Searches for thinking frameworks by keyword.
    """
    return cogni_scaffold.search(keyword)

@mcp.tool
def get_template(name: str) -> str:
    """
    Gets the markdown template for a specific thinking framework.
    """
    return cogni_scaffold.get_template(name)

@mcp.tool
def suggest(problem_description: str) -> list[dict]:
    """
    Suggests relevant thinking frameworks for a given problem description.
    """
    return cogni_scaffold.suggest(problem_description)
