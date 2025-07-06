from mcp.server.fastmcp import FastMCP

mcp=FastMCP("TimeServer")

@mcp.tool()
    
def Time():
    """Get the current date and time in Egypt."""
    import datetime, pytz
    tz = pytz.timezone('Africa/Cairo')
    return datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

if __name__=="__main__":
    mcp.run(transport="stdio")