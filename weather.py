from mcp.server.fastmcp import FastMCP
import requests

mcp=FastMCP("WeatherServer")

# Set your OpenWeatherMap API key here
OPENWEATHERMAP_API_KEY = "OPENWEATHERMAP_API_KEY"

@mcp.tool()

def get_weather(location: str='egypt') -> str:
    """Get weather for a location using OpenWeatherMap API."""
    if not OPENWEATHERMAP_API_KEY:
        return "Weather API key not configured. Please set OPENWEATHERMAP_API_KEY environment variable."
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={OPENWEATHERMAP_API_KEY}&units=metric"
        response = requests.get(url)
            
        if response.status_code == 200:
            data = response.json()
            temp = data["main"]["temp"]
            condition = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            return f"Weather in {location}: {condition.capitalize()}, {temp}°C, Humidity: {humidity}%"
        else:
            return f"Weather data for {location} not available. Error: {response.status_code}"
    except Exception as e:
        return f"Error getting weather for {location}. Please check the location name and try again."
    

if __name__=="__main__":
    mcp.run(transport="stdio")
