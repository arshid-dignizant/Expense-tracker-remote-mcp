from fastmcp import FastMCP
import os


mcp = FastMCP(name="expense-tracker-remote")

@mcp.tool()
def add_number(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)