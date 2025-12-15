import socket

host="127.0.0.1"
port=5060

Countries=["au", "ca", "jp", "ae", "sa", "kr", "us", "ma"]
Languages=["ar", "en" ]
Categories=["business", "general", "health", "science", "sports", "technology" ]

def display_Main_Menu():
    print("\n"+"*"*15+"The Main Menu"+"*"*15)
    print("""1.Search headlines 
2.List of Sources
3.Quit """)
    print("*"*30)



display_Main_Menu()
