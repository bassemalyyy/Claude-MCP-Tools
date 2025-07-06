from mcp.server.fastmcp import FastMCP

mcp=FastMCP("LocationServer")

@mcp.tool()

def location():
    """Get location based on public IP."""
    import geocoder
    g = geocoder.ip('me')
    return g.address if g.ok and g.address else "Address not found."

if __name__=="__main__":
    mcp.run(transport="stdio")