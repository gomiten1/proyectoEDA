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
    with open('users copy.csv', 'r') as file:
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

def check_username_exists(username, filepath):
    with open(filepath, mode='r',newline='') as usersReadFile:
        reader = csv.reader(usersReadFile)
        existing_usernames = [row[0] for row in reader]
    return username in existing_usernames 

def signup():
    filepath = 'users copy.csv'

    newUsername = str(input('Enter your username: '))

    if check_username_exists(newUsername, filepath):
        print('Username already exists.')
        return False

    newPassword = str(input('Enter your password: '))

    user = [newUsername, newPassword]
    with open(filepath, mode = 'a', newline='') as usersWriteFile:
        writer = csv.writer(usersWriteFile)
        writer.writerow(user)
        return True

def administer_trips():
    pass

def search_elements():
    pass

def registerElements():
    menu = int(input("1. Cliente 2. Scooter 3. Station"))
    if menu == 1:
        pass #arbol?
    elif menu == 2:
        pass #lista?
    elif menu == 3:
        pass #grafo?
    else:
        print("Please, choose a valid option")
    
if __name__ == "__main__":
    while True:
        while True:
            
            print("\n\nWelcome, please select one of the options")
            menuLogin = int(input("1. Create account 2. Log in"))
            
            if menuLogin == 1:
                if signup():
                    break
                else:
                    pass
            elif menuLogin == 2:
                user = login()
                break
            else:
                print("Please input valid option")
        
        print("Login successful!")
        
        while True:
        
            menuOption = int(input("1. Register elements 2. Administer trips 3. Search elements 4. Exit"))
            
            if menuOption == 1: 
                registerElements()
            elif menuOption == 2:
                administer_trips()
            elif menuOption == 3:
                search_elements()
            elif menuOption == 4:
                break
        
    
    