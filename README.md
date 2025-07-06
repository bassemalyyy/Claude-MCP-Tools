# Claude MCP

This project sets up a desktop application using Claude, integrated with multiple MCP (Message Control Protocol) servers to provide various functionalities such as greeting, file counting, location detection, web searching, weather updates, and time retrieval. Below is a comprehensive guide to setting up and running the project.

# Video Demo

https://github.com/user-attachments/assets/a4cc82ea-aad5-4815-a799-5f0c8dca9685


# Project Overview
## Requirements
### Setup Instructions
- Step 1: Install Python and Virtual Environment
- Step 2: Install Claude Desktop Application
- Step 3: Set Up the Project Directory
- Step 4: Install Dependencies
- Step 5: Configure MCP Servers
- Step 6: Run the Claude Desktop Application
- MCP Server Details
- Troubleshooting

# Project Overview
The Claude MCP is a Python-based project that integrates with the Claude desktop application to provide a suite of tools accessible via a single interface. The tools are implemented as MCP servers, each handling a specific task:

| Tools | Function |
| ----- | -------- |
| Greeter | Responds to greetings with a personalized message. |
| FileCounter | Counts files on the user's desktop. |
| Location | Retrieves the user's location based on their public IP. |
| Serper | Performs web searches using the Serper.dev API. |
| Weather | Fetches weather data for a specified location using the OpenWeatherMap API. |
| Time | Returns the current date and time in Egypt. |

These tools are connected to Claude via a configuration file (claude_desktop_config.json).
Requirements
To set up and run this project, you need the following:

- Python 3.8 or higher: The project is built using Python.
- Claude Desktop Application: Required to interact with the MCP servers.
- Virtual Environment (recommended): To manage Python dependencies.
- API Keys:
> `OpenWeatherMap API key for the weather.py tool.`

> `Serper.dev API key for the serper.py tool.`


## Python Libraries:
- fastmcp (for MCP server functionality)
- requests (for API calls)
- geocoder (for location detection)
- langchain_community (for search functionality)
- pytz (for time zone handling)


**Operating System: Windows (based on the default file paths in the scripts), though adaptable to macOS/Linux with path adjustments.**

## Setup Instructions
### Step 1: Install Python and Virtual Environment

1- Download and Install Python:
Visit python.org and download Python 3.8 or higher.
Install Python, ensuring you check the option to add Python to your system PATH.


2- Set Up a Virtual Environment:
Open a terminal or command prompt.
Create a virtual environment:

```sh
python -m venv myenv
```

3- Activate the virtual environment:

On Windows:

```sh
myenv\Scripts\activate
```

On macOS/Linux:
```sh
source myenv/bin/activate
```

### Step 2: Install Claude Desktop Application

Download Claude:
Go to the Official [Claude Website](https://claude.ai/download) to download it.

Follow the installation instructions specific to your operating system.
Ensure Claude is configured to support MCP server integration (refer to Claude's documentation for MCP setup).

### Step 3: Set Up the Project Directory

1- Create Project Folder:

Create a directory for the project, e.g., **mcp-test**
Place all provided Python scripts (**greeter.py**, **filecounter.py**, **location.py**, **serper.py**, **weather.py**, **time.py**) in this folder.


2-Create Configuration File:

Open the installation location of Claude Desktop, and find the **claude_desktop_config.json** then, update the file paths in this file to match your system’s Python executable and script locations. Example:

```sh
configuration:{
    "mcpServers": {
        "greeter": {
            "command": "path/to/myenv/Scripts/python.exe",
            "args": ["path/to/mcp-test/greeter.py"]
        },
        "filecounter": {
            "command": "path/to/myenv/Scripts/python.exe",
            "args": ["path/to/mcp-test/filecounter.py"]
        },
        "location": {
            "command": "path/to/myenv/Scripts/python.exe",
            "args": ["path/to/mcp-test/location.py"]
        },
        "serper": {
            "command": "path/to/myenv/Scripts/python.exe",
            "args": ["path/to/mcp-test/serper.py"]
        },
        "weather": {
            "command": "path/to/myenv/Scripts/python.exe",
            "args": ["path/to/mcp-test/weather.py"]
        },
        "time": {
            "command": "path/to/myenv/Scripts/python.exe",
            "args": ["path/to/mcp-test/time.py"]
        }
    }
}
```

### Step 4: Install Dependencies

1- Activate the Virtual Environment (if not already activated).

2- Install Required Libraries:
Run the following commands in the terminal:

```sh
pip install fastmcp requests geocoder langchain-community pytz
```

3- Set Up API Keys:
- OpenWeatherMap API Key:
Sign up at openweathermap.org to obtain an API key.
Replace the OPENWEATHERMAP_API_KEY in weather.py with your key, or set it as an environment variable:

```sh
export OPENWEATHERMAP_API_KEY="your_api_key"  # macOS/Linux
set OPENWEATHERMAP_API_KEY=your_api_key       # Windows
```

- Serper.dev API Key:
Sign up at serper.dev to obtain an API key.
Replace the SERPER_API_KEY in serper.py with your key, or set it as an environment variable:

```sh
export SERPER_API_KEY="your_api_key"  # macOS/Linux
set SERPER_API_KEY=your_api_key       # Windows
```

### Step 5: Configure MCP Servers

Verify MCP Server Scripts:

Ensure all Python scripts (**greeter.py**, **filecounter.py**, **location.py**, **serper.py**, **weather.py**, **time.py**) are in the project directory.

Confirm that the fastmcp library is correctly installed and accessible.


- Test Individual MCP Servers (optional):
Run each script individually to ensure it works:

```sh
python path/to/mcp-test/greeter.py
```

Repeat for other scripts to verify functionality.


### Step 6: Run the Claude Desktop Application

- Launch Claude:

Open the Claude desktop application.

Load the claude_desktop_config.json file in Claude to register the MCP servers.


- Interact with Claude:

Use Claude’s interface to send commands to the MCP servers.

**Example commands:**
- hi, hey, or hello to trigger the greeter.

- count_desktop_files() to count files on the desktop.

- location() to get the current location.

- search("query") to perform a web search.

- get_weather("city") to get weather updates.

- Time() to get the current time in Egypt.


### MCP Server Details

- greeter.py: Responds to hi, hey, or hello with a welcome message.

- filecounter.py: Counts files on the desktop (default path: C:/Users/YourUsername/Desktop).

- location.py: Uses the geocoder library to fetch the user’s location based on their public IP.

- serper.py: Performs web searches using the Serper.dev API (requires an API key).

- weather.py: Fetches weather data using the OpenWeatherMap API (requires an API key).

- time.py: Returns the current date and time in Egypt (Africa/Cairo timezone).

### Troubleshooting

**MCP Server Not Responding:**
- Ensure the Python scripts are in the correct project directory.
- Verify that the virtual environment is activated and dependencies are installed.


**API Key Errors:**
- Double-check that the OPENWEATHERMAP_API_KEY and SERPER_API_KEY are correctly set in the scripts or as environment variables.


**Claude Not Connecting:**
- Confirm that the claude_desktop_config.json file paths match your system’s setup.
- Check Claude’s documentation for MCP server integration issues.


**File Path Issues:**
- Adjust the desktop path in filecounter.py if your desktop is located elsewhere.
- Update claude_desktop_config.json paths for macOS/Linux if needed.
