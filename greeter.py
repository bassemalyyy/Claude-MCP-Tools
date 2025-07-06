from mcp.server.fastmcp import FastMCP

# Create an MCP server named "Greeter"
mcp = FastMCP("Greeter")

@mcp.tool()
def greet(query: str) -> str:
    """Return this welcome message, when greeted with "Hi", "Hey" or "Hello"."""
    if query.lower() == "hi" or query.lower() == "hey" or query.lower() == "hello":
        return "Hello Bassem, I'm Titan, your personal assistant. I can help you with various tasks like searching the web, getting weather updates, and more. Just ask me anything!"

if __name__ == "__main__":
    mcp.run()