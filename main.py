#las funciones y esas cosas las ponemos mejor en otros archivos e importamos
import csv
from Scooter import Scooter
from Client import Client
from User import User
from os import system, name
from Tree.Tree import BTree
from Tree.TreeNode import Data
from Graph.Graph import Graph
from Search.BinarySearch import binary_search
import Sort.RadixSort

def clear_screen():
 
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')
        
       
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

def check_username_exists(username, filepath):
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        next(reader) 
        for row in reader:
            if row and row[0] == username:
                return False
        return True

def signup():
    filepath = 'users.csv'
    while True: 
        newUsername = str(input('Enter your username: '))
    
        if check_username_exists(newUsername, filepath):
            break
        print("Username already exits!")

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
            origin = stations.get_station(scooter.origin)
            name_destination = input("Where are you planning to go?")
            destination = stations.find_station(name_destination)
            
            scooter.destination = stations.find_num_station(name_destination)
            print("Started trip from: " + origin.name + " to itended destination: " + destination.name)
            scooter.cost = stations.find_cost(origin.name, destination.name)
            print("Estimated cost of trip: " + scooter.cost)
            
            
            break
        elif menu == 2:
            destination = stations.get_station(scooter.destination)
            print("Scheduled to arrive to: " + destination.name)
            if 2 == int(input("1. Confirm destination 2. Change destination: ")):
                key_destination = input("New destination: ")
                destination = stations.find_station(key_destination)
                origin = stations.get_station(scooter.origin)
                print("Calculating new cost")
                scooter.cost = stations.find_cost(origin.name, destination.name)
                print("Trip by: " + " from " + origin.name 
                      + " to " + destination.name + "cost: " + scooter.cost)
                print("Your trip will be charged, thank you")
            else:
                origin = stations.get_station(scooter.origin)
                print("Trip by: "  + " from " + origin.name 
                      + " to " + destination.name + "cost: " + scooter.cost)
                print("Your trip will be charged, thank you")
            
            scooter.origin = scooter.destination
            scooter.destination = None
            scooter.client = None  
            scooter.cost = 0  
            break
        else:
            print("Invalid option")
    




def fill_tree_clients(tree):
    with open('client.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader) 
        id = 0
        for row in reader:
            obj = Client(int(row[0]), row[1], row[2], row[3], row[4], row[5])
            tree.insert(Data(obj.id, obj))
            id += 1
    return id
def fill_tree_scooters(tree):
    with open('scooters.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader) 
        id = 0
        for row in reader:
            obj = Scooter(int(row[0]),origin= int(row[1]))
            tree.insert(Data(obj.id, obj))
            id += 1
    return id

    
    
if __name__ == "__main__":
    tree_scooters = BTree(2)
    num_scooters = fill_tree_scooters(tree_scooters)
    tree_clients = BTree(2)
    num_clients = fill_tree_clients(tree_clients)
    map_stations = Graph(20, 30, 2, 1)
    map_stations.read_edges_from_csv("graph.csv")
    
    
    
    while True:
        while True:
            
            print("\n\nWelcome, please select one of the options")
            menuLogin = int(input("1. Create account 2. Log in 3. Exit: "))
            
            if menuLogin == 1:
                user = signup()
                break
            elif menuLogin == 2:
                user = login()
                break
            elif menuLogin == 3:
                break
            else:
                print("Please input valid option")
                
        if menuLogin == 3:
            break
    
        
        print("Login successful!")
        
        while True:
        
            menuOption = int(input("1. Register elements 2. Administer trips 3. Search elements 4. Delete elements 5. Exit"))
            
            if menuOption == 1: 
                menuRegister = int(input("1. Cliente 2. Scooter"))
                if menuRegister == 1:
                    
                    
                 
                    num_clients += 1                    
                    id = num_clients
                    name = input("Name: ")
                    address = input("Address: ")
                    phone = input("# Phone: ")
                    mail = input("Mail: ")
                    card_data = input("Card data: ")
                    insert = Client(id, name, address, phone, mail, card_data)
                    tree_clients.insert(Data(insert.id, insert))
                    print("Client: ")
                    print(insert)
                    
                    try:
                        file = open("client.csv", "a", encoding='utf-8')
                        file.write(str(id)+","+name+","+address+","+phone+","+mail+","+card_data+"\n")
                        print("Client created successfully")
                    except:
                        print("Error: file not found")
                    finally:
                        if file:
                            file.close()
               
                    
                elif menuRegister == 2:
                    
                    print("Creating new scooter")
                    num_scooters += 1
                    id = num_scooters
                    key_station = input("Station where scooter is stored: ")
                    print("The scooter is being registered")
                    new_scooter = Scooter(id)

                    tree_scooters.insert(Data(new_scooter.id,new_scooter))
                    station_update = map_stations.find_station(key_station)
                    station_key = map_stations.find_num_station(key_station)
                    
                    station_update.scooters.append(new_scooter)
                    Sort.RadixSort.radixSortID(station_update.scooters)
                    
                    try:
                        file = open("scooters.csv", "a", encoding='utf-8')
                        file.write(str(id)+","+str(station_key)+",,,"+"\n")
                        print("Registered globally successfully")
                    except:
                        print("Error: file not found")
                    finally:
                        if file:
                            file.close()
                    
                    
                    
                    #Para guardarlo en el archivo (grafo) poner código
                    
                    
                    
                else:
                    print("Please, choose a valid option")
            elif menuOption == 2:
                id_scooter = int(input("Enter ID of scooter: "))
                rented_scooter = tree_scooters.search(id_scooter)
                id_client = int(input("Enter ID of client: "))
                client = tree_clients.search(id_client)
                administer_trips(map_stations, client, rented_scooter)
            
            
            elif menuOption == 3:
                menuSearch = int(input("1. Scooter globally 2. Scooter locally (Within a station) 3. Client"))
                
                if menuSearch == 1:
                    while True:
                        id_scooter = int(input("ID of scooter: "))
                        found_scooter = tree_scooters.search(id_scooter)
                        if found_scooter != None:
                            print("Found scooter")
                            print(found_scooter)
                            break
                        else:
                            print("Scooter not found")
                            if 2 == int(input("1. Try again 2. Exit")):
                                break
                        
                        
                
                elif menuSearch == 2:
                    while True: 
                        key_station = input("Name of station to search: ")
                        search_station = map_stations.find_station(key_station)
                        id_scooter = int(input("ID of scooter: "))
                        found_scooter = binary_search(search_station.scooters, id_scooter)
                        if found_scooter != None:
                            print("Found scooter")
                            print(found_scooter)
                            break
                        else:
                            print("Scooter not found")
                            if 2 == int(input("1. Try again 2. Exit")):
                                break
                        
                        
                        
                elif menuSearch == 3:
                    while True: 
                        id_client = int(input("ID of client: "))
                        found_client = tree_clients.search(id_client)
                        if found_client != None:
                            print("Found client")
                            print(found_client)
                            break
                        else:
                            print("Client not found")
                            if 2 == int(input("1. Try again 2. Exit")):
                                break
     
                    
                '''elif menuOption == 4:
                menuDelete = int(input("1. Scooter 2. Client"))
                if menuDelete == 1:
                    delete = int(input("Id: "))
                    index = 0
                    with open('scooters.csv', 'r') as file:
                        rows = list(csv.reader(file))
                        
                    
                    while delete != rows[index][0]:
                        index += 1

                    del rows[index]

                    
                    with open('scooters.csv', 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(rows)
                        
                    tree_scooters = BTree(2)
                    num_scooters = fill_tree_scooters(tree_scooters)
                    map_stations = Graph(20, 30, 2, 1)
                    map_stations.read_edges_from_csv("graph.csv")
                elif menuDelete == 2:
                    delete = int(input("Id: "))
                    index = 0
                    with open('client.csv', 'r') as file:
                        rows = list(csv.reader(file))
                        
                    
                    while delete != rows[index][0]:
                        index += 1

                    del rows[index]

                    
                    with open('client.csv', 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(rows)
                    tree_clients = BTree(2)
                    num_clients = fill_tree_clients(tree_clients)'''    

                    
            elif menuOption == 5:    
                break
            else:
                print("Invalid option, please try again")
        
        
    