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

# Takes a list of articles form that returned from fetch_headlines(),
# extract these details (source name,authour,title)
# and adds at the beggiing an index for each article 
def get_headlines_brief(articles):
    brief_list = []
    for i, article in enumerate(articles):
        brief = {
            "index" : i+1,
            # add {} empty value as default for no source and N/A if the source is none ,so it does not crash
            "source_name": article.get("source",{}).get("nmae","N/A"),
            "author": article.get("author"),
            "title": article.get("title")
        }
        brief_list.append(brief)
    return brief_list

#  takes a single article from the stored list,
#  extracts all 7 details (source name, author, title, URL, description, publish date, publish time),
#  and returns them as a dictionary to send to the client
def get_headline_details(article):
    # split date and time
    published_at = article.get("publishedAt", None) # set the date to null if there is no one
    # check if publish date exit
    if published_at:
        date_part = published_at[0:10]
        time_part = published_at[11:19]
    else:
        date_part = "N/A" # for display
        time_part = "N/A"
    details = {
        "source_name": article.get("source", {}).get("name", "N/A"),
        "author": article.get("author", "N/A"), # for display
        "title": article.get("title", "N/A"),
        "url": article.get("url", "N/A"),
        "description": article.get("description", "N/A"),
        "publish_date": date_part,
        "publish_time": time_part
    }
    return details


# takes the list of sources teturned by fetch_sources(),
# extract these details (ourcename)
# adds an indext at the begging then return the list
def get_sources_brief(sources):
    brif_list = []
    for i,source in enumerate(sources): # enumerate() puts an index to each element in a list and represented as i 
        brief = {
            "index": i+1,
            "source_name": source.get("name", "N/A")
        }
        brif_list.append(brief)
    return brif_list

# takes a single source from the stored list,
# extracts all 6 details (source name, country, description, URL, category, language),
# and returns them as a dictionary to send to the client.
def get_source_details(source):
    details = {
        "source_name": source.get("name", "N/A"),
        "country": source.get("country", "N/A"),
        "description": source.get("description", "N/A"),
        "url": source.get("url", "N/A"),
        "category": source.get("category", "N/A"),
        "language": source.get("language", "N/A")
    }
    return details



def handle_client(client_socket, client_address):

    client_name = None
    
    current_headlines = []
    current_sources = []
    
    try:
        
        client_name = client_socket.recv(1024).decode().strip()
        
        
        print(f"\n[+] NEW CONNECTION: {client_name} from {client_address}")
        
        
        client_socket.send("Connected to server successfully".encode())
        

        while True:

            request = client_socket.recv(4096).decode().strip()
            
            if not request:
                break
            
            
            try:
                request_data = json.loads(request)
            except json.JSONDecodeError:
                client_socket.send(json.dumps({"error": "Invalid request format"}).encode())
                continue
            
            request_type = request_data.get("type", "")
            option = request_data.get("option", "")
            value = request_data.get("value", "")
            
            print(f"[REQUEST] Client: {client_name} | Type: {request_type} | Option: {option} | Value: {value}")
            

            if request_type == "quit":
                client_socket.send(json.dumps({"status": "goodbye"}).encode())
                break
            

            
            if request_type == "headlines":
                current_headlines = fetch_headlines(option, value)
                
     
                save_to_JSON(client_name, f"headlines_{option}", current_headlines)
                
                brief_list = get_headlines_brief(current_headlines)
                response = {
                    "status": "success",
                    "type": "headlines_list",
                    "data": brief_list
                }
                client_socket.send(json.dumps(response).encode())
            

            elif request_type == "sources":
                current_sources = fetch_sources(option, value)
                
                save_to_JSON(client_name, f"sources_{option}", current_sources)
                
                brief_list = get_sources_brief(current_sources)
                response = {
                    "status": "success",
                    "type": "sources_list",
                    "data": brief_list
                }
                client_socket.send(json.dumps(response).encode())
            

            
            elif request_type == "headline_details":
                index = int(request_data.get("index", 1)) - 1  
                if 0 <= index < len(current_headlines):
                    details = get_headline_details(current_headlines[index])
                    response = {
                        "status": "success",
                        "type": "headline_details",
                        "data": details
                    }
                else:
                    response = {"status": "error", "message": "Invalid index"}
                client_socket.send(json.dumps(response).encode())
            
            elif request_type == "source_details":
                index = int(request_data.get("index", 1)) - 1 
                if 0 <= index < len(current_sources):
                    details = get_source_details(current_sources[index])
                    response = {
                        "status": "success",
                        "type": "source_details",
                        "data": details
                    }
                else:
                    response = {"status": "error", "message": "Invalid index"}
                client_socket.send(json.dumps(response).encode())
            
            else:
                response = {"status": "error", "message": "Unknown request type"}
                client_socket.send(json.dumps(response).encode())
    
    except Exception as e:
        print(f"[ERROR] {client_name}: {e}")
    
    finally:
        
        print(f"[-] DISCONNECTED: {client_name}")
        client_socket.close()


def main():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    

    server_socket.bind((host, port))
    server_socket.listen(5)
    
    print("=" * 50)
    print("       NEWS SERVICE SERVER")
    print("=" * 50)
    print(f"[*] Server started on {host}:{port}")
    print("[*] Waiting for connections...")
    print("=" * 50)
    
    try:
        while True:

            client_socket, client_address = server_socket.accept()
            

            client_thread = threading.Thread(
                target=handle_client,
                args=(client_socket, client_address)
            )
            client_thread.start()
            
            print(f"[*] Active connections: {threading.active_count() - 1}")
    
    except KeyboardInterrupt:
        print("\n[*] Server shutting down...")
    
    finally:
        server_socket.close()


if __name__ == "__main__":
    main()