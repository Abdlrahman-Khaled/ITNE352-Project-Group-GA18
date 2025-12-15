import socket

host="127.0.0.1"
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


display_Headlines_Menu()
display_Sources_Menu()
