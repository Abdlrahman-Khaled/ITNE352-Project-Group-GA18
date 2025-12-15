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


def main():
    CSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

   # CSocket.connect((hostIP,port))
    print("\n"+"*"*15+" NEWS SERVICE SERVER "+"*"*15)
    Cname=input("Enter your name :")
    # CSocket.sendall(Cname.encode("UTF-8"))
    #response=CSocket.recv(2048).decode("UTF-8")
    #print("server:"+response)

    while True:
        try:
            display_Main_Menu()
            user_Choice=input("Enter your choice(1,2,or 3):")

            if user_Choice=="1":
                pass
            elif user_Choice=="2":
                pass
            elif user_Choice=="3":
                pass
            else:
                print("Invalid choice")

        except ConnectionRefusedError:
            print("can't connect to server,The server is runing?")
        except Exception as E:
            print("The Error is : ",E)
        finally:
         CSocket.close()

main()


