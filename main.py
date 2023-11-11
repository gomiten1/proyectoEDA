#las funciones y esas cosas las ponemos mejor en otros archivos e importamos
import csv
from os import system, name

def clear_screen():
 
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')
        
class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        
def authenticate_user(username, password):
    with open('users.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader) 
        for row in reader:
            if row and row[0] == username and row[1] == password:
                user = User(row[0], row[1])
                return user

def login():
    print("Please enter your credentials")
    username = input("Username: ")
    password = input("Password: ")
    user = None
    user = authenticate_user(username, password)
    while user == None:
        print("Invalid username or password")
        print("Reenter credentials")
        username = input("Username: ")
        password = input("Password: ")
        user = authenticate_user(username, password)
    
    clear_screen()
    return user

def signup():
    pass
    
if __name__ == "__main__":
    while True:
        
        print("\n\nWelcome, please select one of the options")
        menuLogin = int(input("1. Create account 2. Log in"))
        
        if menuLogin == 1:
            signup()
            break
        elif menuLogin == 2:
            user = login()
            break
        else:
            print("Please input valid option")
    
    print("Login successful!")
    
    
    
    