import json
import socket

hostIP="127.0.0.1"
port=5060

Countries=["au", "ca", "jp", "ae", "sa", "kr", "us", "ma"]
Languages=["ar", "en" ]
Categories=["business", "general", "health", "science", "sports", "technology" ]

def display_Main_Menu():
    print("\n"+"*"*15+" The Main Menu "+"*"*15)
    print("""1.Search headlines 
2.List of Sources
3.Quit """)
    print("*"*30)



def display_Headlines_Menu():
    print("\n"+"*"*15+" The Headlines Menu "+"*"*15)
    print("""1.Search for keywords   
2.Search by category     
3.Search by country    
4.List all new headlines  
5.Back to the main menu    """)
    print("*"*50)



def display_Sources_Menu():
    print("\n"+"*"*15+" The Sources Menu "+"*"*15)
    print("""1.Search by category   
2.Search by country     
3.Search by language    
4.List all 
5.Back to the main menu    """)
    print("*"*50)


def display_Countries():
    print("\nCountries: ")
    for num,countri in enumerate(Countries,1):
        print(f"{num}.{countri}")


def display_Categories():
    print("\nCategories: ")
    for num,categ in enumerate(Categories,1):
        print(f"{num}.{categ}")




def display_Languages():
    print("\nLanguages: ")
    for num,lang in enumerate(Languages,1):
        print(f"{num}.{lang}")




def display_Headlies_List(data):
    print("\n"+"*"*15+" Headlines "+"*"*15)

    if not data:
        print("Can't found results. ")
        return
    for item in data:
        print(f"\n[{item["index"]}]")
        print(f"Source: {item["source_Name"]}")
        print(f"Author: {item["author"]}")
        print(f"Title: {item["title"]}")
    print("*"*50)



def display_Headlines_Details(data):
    print("\n"+"*"*15+" Headlines Details "+"*"*15)

    print(f"name: {data['source_name']}")
    print(f"Country: {data['country']}")
    print(f"Description: {data['description']}")
    print(f"URL: {data['URL']}")
    print(f"Category: {data['Category']}")
    print(f"Language: {data['Language']}")

    print("*"*50)






def get_Choice(prompt, Max_Value):
    while True:

        try:
            user_Choice =int(input(prompt))
            if 1 <= user_Choice<= Max_Value:
                return user_Choice
            print(f"Enter number between 1 and {Max_Value}: ")
        except:
            print("Invalid input.Enter number")

def send_Request(CSocket,request):
    CSocket.send(json.dumps(request).encode("UTF-8"))
    response=CSocket.recv(10000).decode()
    return json.loads(response)

def handle_Headlines_Menu(CSocket):
    while True:
        display_Headlines_Menu()
        uesr_Choice=input("Enter your choice (1-5): ")

        request=None

        if uesr_Choice=="1":
            keyword=input("enter keyword: ")
            request={"type":"headlines", "option":"keyword","value":keyword}

        elif uesr_Choice=="2":
            display_Categories()
            index=get_Choice("Select country(1-8):",8)

        elif uesr_Choice =="3":
            display_Countries()
            index=get_Choice("Select country(1-8):",8)
            request={"type":"Headlines","option":"country","value":Countries[index-1]}

        elif uesr_Choice =="4":
            request={"type":"Headlines","option":"all","value":""}


        elif uesr_Choice =="5":
            return
        else:
            print("Invalid value")
            continue

        if request:

            response=send_Request(CSocket,request)

            if response.get("status")== "success" :
                headlines=response.get("data" ,[])
                display_Headlies_List(headlines)

                if headlines:
                    detail =input("\nenter number for details or (0 to skip)")
                    if detail !="0":
                        datail_Request={"type":"headline_Details","index":detail}
                        detail_Response=send_Request(CSocket,datail_Request)

                        if detail_Response.get("status")=="success":
                            display_Headlines_Details(detail_Response.get("data",{ }))

                        else:
                            print("Error geting details")
            else:
                print("Error: " + response.get("message", "Unknown Error"))






def display_Sources_List(data):
    print("\n"+"*"*15+" Sources "+"*"*15)

    if not data:
        print("Can't found results. ")
        return
    for item in data:
        print(f"[{item['index']}]{item['source_name']}")

    print("*"*50)



def display_Sources_Details(data):
    print("\n"+"*"*15+" Sources Details "+"*"*15)

    print(f"name: {data['source_name']}")
    print(f"Country: {data['country']}")
    print(f"Description: {data['description']}")
    print(f"URL: {data['URL']}")
    print(f"Category: {data['Category']}")
    print(f"Language: {data['Language']}")

    print("*"*50)





def handle_Sources_Menu(CSocket):
    while True:
        display_Sources_Menu()
        uesr_Choice = input("Enter your choice (1-5): ")

        request = None

        if uesr_Choice == "1":
            display_Categories()
            index = get_Choice("Select category(1-6)",6)
            request = {"type": "sources", "option": "category", "value": Categories[index-1]}

        elif uesr_Choice == "2":
            display_Countries()
            index = get_Choice("Select country(1-8):", 8)
            request = {"type": "sources", "option": "country", "value": Countries[index-1]}


        elif uesr_Choice == "3":
            display_Languages()
            index = get_Choice("Select languages(1-2):", 2)
            request = {"type": "sources", "option": "languages", "value": Languages[index - 1]}

        elif uesr_Choice == "4":
            request = {"type": "sources", "option": "all", "value": ""}


        elif uesr_Choice == "5":
            return

        else:
            print("Invalid value")
            continue

        if request:

            response = send_Request(CSocket, request)

            if response.get("status") == "success":
                sources = response.get("data", [])
                display_Sources_List(sources)

                if sources:
                    detail = input("\nenter number for details or (0 to skip)")
                    if detail != "0":
                        datail_Request = {"type": "source_details", "index": detail}
                        detail_Response = send_Request(CSocket, datail_Request)

                        if detail_Response.get("status") == "success":
                            display_Sources_Details(detail_Response.get("data", {}))


                        else:
                            print("Error geting details")
            else:
                print("Error: " + response.get("message", "Unknown Error"))

#display_Categories

def main():
    CSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
            CSocket.connect((hostIP,port))
            print("\n"+"*"*15+" NEWS SERVICE CLIENT "+"*"*15)
            Cname=input("Enter your name :")
            CSocket.sendall(Cname.encode("UTF-8"))
            response=CSocket.recv(2048).decode("UTF-8")
            print("server:"+response)

            while True:

                display_Main_Menu()
                user_Choice=input("Enter your choice(1,2,or 3):")

                if user_Choice=="1":
                    handle_Headlines_Menu(CSocket)
                elif user_Choice=="2":
                    handle_Sources_Menu(CSocket)
                elif user_Choice=="3":
                    quit={"type":"quit"}
                    CSocket.send(json.dumps(quit).encode("UTF-8"))
                    print("\nBye")
                    break
                else:
                     print("Invalid choice")

    except ConnectionRefusedError:
        print("can't connect to server,The server is runing?")
    except Exception as E:
        print("The Error is : ",E)
    finally:
        CSocket.close()


if __name__ =="__main__":
    main()


