# fully news system

## News Service System

A client-server system that retrieves news from NewsAPI. The server fetches news and handles mutiples clients. The client displays menus and shows news.

## Semester
S1 2025-2026

## Group:
| | |
|---|---|
| Group Name | GA18|
| Course Code | ITNE352 |
| Section|1|
| Abdulrahman Khaled Saleh | 202308169 |
| Ali Jaber Ateya Husain | 202104610 |

## Table of Contents

1. Requirements
2. How to Run
3. The Scripts
4. Additional Concepts
5. Acknowledgments
6. Conclusion

## Requirements

- python 3
- Internet connection
- NewsAPI key form newsapi.org - https://newsapi.org/

All libraries are built-in:
- import:
	- socket
	- threading
	- json
	- urllib.request
	- urllib.error


## How to Run

1. Put your API key in 'server.py' (I have put my API Key)

2. Run server: python server.py

3. run client (in new terminal): python client.py

4. Enter your name and use the menus   


## Scripts Description

### server.py
- Listens on port 5000
- Handles multiple clients using threads
- Fetches news from NewsAPI
- Saves results to JSON files

**server functions
| Function | What it does |
|----------|--------------|
| `fetch_headlines()` | Gets news headlines from API |
| `fetch_sources()` | Gets news sources from API |
| `save_to_JSON()` | Saves data to JSON file |
| `get_headlines_brief()` | Gets brief headline info (source, author, title) |
| `get_headline_details()` | Gets full headline info |
| `get_sources_brief()` | Gets brief source info (name only) |
| `get_source_details()` | Gets full source info |
| `handle_client()` | Handles one client connection |
| `main()` | Starts server and accepts connections, and does not run the server if the file is imported unless it calls the main() function |

### client.py

| Function | What it does |
|----------|--------------|
| `display_Main_Menu()` | Shows main menu |
| `display_Headlines_Menu()` | Shows headlines menu |
| `display_categories()` | Shows list of 6 categories for user to select |
| `display_countries()` | Shows list of 8 countries for user to select |
| `display_languages()` | Shows list of 2 languages for user to select |
| `display_headlines_list()` | Displays brief list of headlines (source, author, title) |
| `display_Sources_List()` | Displays brief list of sources (name only) |
| `display_Sources_Menu()` | Shows sources menu |
| `send_request()` | Sends JSON request to server and receives JSON response |
| `get_choice()` | Gets and validates numeric input from user (1 to max) |
| `send_Request()` | Sends request to server |
| `handle_Headlines_Menu()` | Handles headlines options |
| `handle_Sources_Menu()` | Handles sources options |
| `main()` | Connects to the server and runs menus, and does not run if the file is imported unless it calls the main() function |


## Additional Concept: 

**Multithreading:** used to handle multiple clients at the same time


```python
client_thread = threading.Thread(target=handle_client,args=(client_socket, client_address))
client_thread.start()
```

## Acknowledgments
- Dr. Mohammed Almeer

## Conclusion
This project shows how to build a client-server system using Python sockets, threading, and API integration.
