import socket
import threading
import json
import urllib.request
import urllib.error

API_key = "da2a3228d31f45f3809df6be622c2749" 
host = "127.0.0.1"
port = 5000
group_id ="GA18"

#This function connects to NewsAPI website and gets
# news headlines based on what the user wants(keyword, category, country, or all)
#returns maximum 15 articles as a list.
def fetch_headlines(option,value=None):

    api_url = "https://newsapi.org/v2/top-headlines?"

    if option == "keyword":
        url = f"{api_url}q={value}&apiKey={API_key}"
    elif option == "category":
        url = f"{api_url}category={value}&apiKey={API_key}"
    elif option == "country":
        url = f"{api_url}country={value}&apiKey={API_key}"
    else:
        url = f"{api_url}country=us&apiKey={API_key}" # set the default country=us
    
    try:
        respon = urllib.request.urlopen(url)
        data = json.loads(respon.read().decode()) # convert it from JSON to python dir to work and access data 
        return data.get("articles",[])[:15]
    except urllib.error.HTTPError as e:
        print(f"HTTP ERROR {e.code} : {e.reason}")
        return [] # returns empty list insted of shut down the program
    except urllib.error.URLError as e:
        print(f" URL ERROR {e.reason}")
        return []
    except json.JSONDecodeError as e:
        print(f"JSON ERROR {e}")
        return []

# connects to NewsAPI, builds the correct URL 
# based on user's choice (category, country, language, or all)
# fetches news sources and returns maximum 15 sources as a list.
def fetch_sources(option,value=None): # set the value as default None
    api_url = "https://newsapi.org/v2/top-headlines/sources?"

    if option == "category":
        url = f"{api_url}category={value}&apiKey={API_key}"
    elif option == "country":
        url = f"{api_url}country={value}&apiKey={API_key}"
    elif option == "language":
        url = f"{api_url}language={value}&apiKey={API_key}"
    else:
        url = f"{api_url}country=us&apiKey={API_key}"

    try:
        respon = urllib.request.urlopen(url)
        data = json.loads(respon.read().decode())
        return data.get("sources",[])[:15]
    
    except urllib.error.HTTPError as e:
        print(f"HTTP ERROR {e.code} : {e.reason}")
        return [] # returns empty list insted of shut down the program
    except urllib.error.URLError as e:
        print(f" URL ERROR {e.reason}")
        return []
    except json.JSONDecodeError as e:
        print(f"JSON ERROR {e}")
        return []

# save the data comes form fetch_sources and fetch_headlines to JSON
# and the format is <client_name>_<option>_<group_ID>.json
def save_to_JSON(client_name, option ,data):
    fileName = f"{client_name}_{option}_{group_id}.json"
    with open(fileName,"w") as file:
        json.dump(data,file,indent=4)
    print(f"FILE Saved as {fileName}")
    return fileName