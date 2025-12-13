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