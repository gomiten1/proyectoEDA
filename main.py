#las funciones y esas cosas las ponemos mejor en otros archivos e importamos
import csv
from Scooter import Scooter
from Client import Client
from User import User
from os import system, name
from Tree.BinaryTree import BinaryTree
from Graph.Graph import Graph
import Search.BinarySearch
import Sort.RadixSort

def clear_screen():
 
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')
        
       
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
    while True: 
        newUsername = str(input('Enter your username: '))
    
        if check_username_exists(newUsername, filepath):
            print('Username already exists.')
            break

    newPassword = str(input('Enter your password: '))

    user = [newUsername, newPassword]
    with open(filepath, mode = 'a', newline='') as usersWriteFile:
        writer = csv.writer(usersWriteFile)
        writer.writerow(user)
        user = User(newUsername, newPassword)
        return user

def administer_trips(stations, client, scooter):
    print("Select the option to administer a trip")
    while True:
        menu = int(input("1. Start a trip 2. End a trip"))
    
        if menu == 1:
            scooter.client = client
            origin = input("In what station are you renting your scooter? ")
            #falta terminar
            
            
            break
        elif menu == 2:
            break
        else:
            print("Invalid option")
    

def search_elements():
    pass


    
    
if __name__ == "__main__":
    tree_scooters = BinaryTree()
    tree_clients = BinaryTree()
    map_stations = Graph(20, 10, 2, 2)
    
    
    
    while True:
        while True:
            
            print("\n\nWelcome, please select one of the options")
            menuLogin = int(input("1. Create account 2. Log in"))
            
            if menuLogin == 1:
                user = signup()
                break
            elif menuLogin == 2:
                user = login()
                break
            else:
                print("Please input valid option")
        
        print("Login successful!")
        
        while True:
        
            menuOption = int(input("1. Register elements 2. Administer trips 3. Search elements 4. Delete elemnts 5. Exit"))
            
            if menuOption == 1: 
                menuRegister = int(input("1. Cliente 2. Scooter 3. Station"))
                if menuRegister == 1:
                    
                    id = int(input("ID of client: "))
                    name = input("Name: ")
                    address = input("Address: ")
                    phone = int(input("# Phone: "))
                    mail = input("Mail: ")
                    card_data = input("Card data: ")
                    tree_clients.insert(Client(id, name, address, phone, mail, card_data))
                    
                    #Guardar en archivo
                    
                elif menuRegister == 2:
                    
                    id = int(input("ID of scooter: "))
                    key_station = input("Station where scooter is stored: ")
                    print("The scooter is being registered")
                    new_scooter = Scooter(id)
                    tree_scooters.insert(new_scooter)
                    station_update = map_stations.find_station(key_station)
                    
                    station_update.scooters.append(new_scooter)
                    Sort.RadixSort.radixSortID(station_update.scooters)
                    
                    
                    
                    
                    
                    #Para guardarlo en el archivo (grafo y arbol) poner código
                    
                elif menuRegister == 3:
                    pass
                    
                    
                else:
                    print("Please, choose a valid option")
            elif menuOption == 2:
                id_scooter = int(input("Enter ID of scooter: "))
                rented_scooter = tree_scooters.search(tree_scooters.root, id_scooter)
                id_client = int(input("Enter ID of client: "))
                client = tree_clients.search(input(tree_clients.root, id_client))
                administer_trips(map_stations, client, rented_scooter)
            elif menuOption == 3:
                menuSearch = int(input("1. Scooter globally 2. Scooter locally (Within a station) 3. Client"))
                if menuSearch == 1:
                    id_scooter = int(input("ID of scooter: "))
                    found_scooter = tree_scooters.search(tree_scooters.root, id_scooter)
                    if found_scooter != None:
                        print("Found scooter")
                        print(found_scooter)
                    else:
                        print("Scooter not found")
                        print("1. Try again 2. Exit")
                        
                        #terminar código acá xdxdxdd
                
                elif menuSearch == 2:
                    key_station = input("Name of station to search: ")
                    search_station = map_stations.find_station(key_station)
                    
                    
                    
                    
            elif menuOption == 4:
                
                break
        
    
    