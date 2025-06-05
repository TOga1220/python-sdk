# server.py
import statistics

from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    return a - b

# Add a multiplication tool
@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

# Add a division tool
@mcp.tool()
def divide(a: int, b: int) -> float:
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# 標準偏差を求めるツールを追加
@mcp.tool()
def stddev(numbers: list[float]) -> float:
    """与えられた数値リストの標準偏差を返す"""
    if len(numbers) < 2:
        raise ValueError("2つ以上の数値が必要です")
    return statistics.stdev(numbers)


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# Add a dynamic greeting resource
@mcp.resource("two://{name}")
def two(name: int) -> str:
    """Get a personalized greeting with name repeated twice"""
    return f"Hello, {name*2}!"

# Add a dynamic greeting resource
@mcp.tool("greeting")
def get_greeting_(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hellotrtqeptaetae, {name}!"