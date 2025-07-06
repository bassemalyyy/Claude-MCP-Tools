from mcp.server.fastmcp import FastMCP
from langchain_community.tools.tavily_search import TavilySearchResults
import requests
import json , datetime

mcp=FastMCP("SerperServer")

# Set your Serper.dev API key here
SERPER_API_KEY = "211769b35c417bd23a4e89764cd847827e0d054b"

@mcp.tool()

def search(query: str) -> str:
    """Perform a web search using Serper.dev."""
    if not SERPER_API_KEY:
        return "Search API key not configured. Please set SERPER_API_KEY environment variable."
        
    try:
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query})
        headers = {
                'X-API-KEY': SERPER_API_KEY,
                'Content-Type': 'application/json'
            }
            
        response = requests.post(url, headers=headers, data=payload)
            
        if response.status_code == 200:
            results = response.json()
                
            if "organic" not in results or not results["organic"]:
                return f"No search results found for '{query}'."
                
            formatted_results = []
                # Get search time
            search_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                # Show more results (5 instead of 3)
            for idx, result in enumerate(results["organic"][:5], 1):
                title = result.get("title", "No title")
                link = result.get("link", "No link")
                snippet = result.get("snippet", "No description")
                formatted_results.append(f"{idx}. {title}\nURL: {link}\nDescription: {snippet}\n")
                
            return f"Search results as of {search_time}:\n\n" + "\n".join(formatted_results)
        else:
            return f"Error searching for '{query}'. Status code: {response.status_code}"
    except Exception as e:
        return f"Error performing search for '{query}'. Please try again later."

if __name__=="__main__":
    mcp.run(transport="stdio")