import csv
import os
from Graph.Station import Station
from Scooter import Scooter

class Graph:
    edges = []
    grade = []
    names = ['','Deneb Algedi', 'Nashira', 'Andromeda', 'Kastra', 'Nunki', 'Ascella', 'Dorsum', 'Alshat', 
             'Algiedi', 'Mabakk', 'Arcab', 'Prior Rukbat', 'Armus', 'Kaus Borealis', 'Kaus Media', 
             'Kaus Australis', 'Galantis', 'Baten', 'Algiedi', 'Dahin']
    locations = ['','5646 Pleasure Pass', '476 Merry Trail', '3 Prentice Trail', '2341 Londonderry Alley', '6417 Beilfuss Street', 
                 '5 Buell Hill', '00885 Fairview Trail', '6 Southridge Park', '162 Sunbrook Place', '4466 Butterfield Hill', 
                 '1 Northwestern Place', '94 Village Street', '7 Luster Place', '406 Meadow Valley Crossing', '16 Brown Pass',
                 '3 Ilene Junction', '48 Fairfield Alley', '01 Vera Crossing', '0532 Vernon Terrace', '86 Melvin Court']

    def __init__(self, numNodes, numEdges, directed, cost):
        self.numNodes = numNodes
        self.numEdges = numEdges
        self.directed = True if directed == 1 else False
        self.hasCost = True if cost == 1 else False

        i = 0
        while i<= self.numNodes:
            self.grade.append(0)
            self.edges.append(None)
            i+=1
    
    def insert_edge(self, intU, intV, intCost, isDirected, scooters = []):
        
        item = Station()
        item.name = self.names[intU]
        item.scooters = scooters
        item.location = self.locations[intU]
        item.cost = intCost
        item.to = intV
        item.nxt = self.edges[intU]
        

        self.edges[intU] = item
        self.grade[intU]+=1

        if isDirected == False and intV != intU:
            self.insert_edge(intV, intU, intCost, True)


    def read_edges(self):
        
        i = 1
        while i <= self.numEdges:
            u = int(input('u: '))
            v = int(input('v: '))

            if self.hasCost == True:
                cost = input('Cost / Weight: ')
            else:
                cost = 1

            self.insert_edge(u, v, cost, self.directed)
            i+=1

    def print(self):
        i = 1
        item = None
        string = ""

        while i <= self.numNodes:
            string += str(i) + "\t"
            item = self.edges[i]

            while item != None:
                string += str(item.to) + ": " + str(item.cost) + "\t"
                item = item.nxt
            
            string+="\n"
            i+=1
        
        print(string)

    def breadth_first_search(self, intSource):
     

        if self.edges[intSource] == None:
            self.edges[intSource] = Station()
        self.edges[intSource].color = 1
        self.edges[intSource].distance = 0
        self.edges[intSource].prev = None
        queue = []
        queue.append(intSource)
        while len(queue) != 0:
            u = queue.pop(0)
            v = self.edges[u]
            while v != None:
                if self.edges[v.to] != None:
                    if self.edges[v.to].color == 0:
                        self.edges[v.to].color = 1
                        self.edges[v.to].distance = self.edges[u].distance + 1
                        self.edges[v.to].prev = u
                        queue.append(v.to)

                v = v.nxt
            self.edges[u].color = 2
            
    def find_cost(self, source, destination):
        intSource = self.find_num_station(source)
        intDestination = self.find_num_station(destination)
        if intSource not in range(1, self.numNodes + 1) or intDestination not in range(1, self.numNodes + 1):
            print("Invalid station ID")
            return None
        if self.edges[intSource] == None:
            self.edges[intSource] = Station()
        self.edges[intSource].color = 1
        self.edges[intSource].distance = 0
        self.edges[intSource].prev = None
        
        
        queue = [(intSource, 0)]
        
        while len(queue) != 0:
            element = queue.pop(0)
            u, accumulated_cost = element
            v = self.edges[u]
            while v != None:
                if self.edges[v.to] != None:
                    if self.edges[v.to].color == 0:
                        self.edges[v.to].color = 1
                        self.edges[v.to].distance = self.edges[u].distance + 1
                        self.edges[v.to].prev = u
                        accumulated_cost += v.cost
                        queue.append((v.to, accumulated_cost))
                        print("Avanzando", v.to)
                        
                        if v.to == intDestination:
                            return accumulated_cost
                v = v.nxt
            self.edges[u].color = 2

    def get_station(self, k):
        return self.edges[k]
        
    def find_station(self, station_name):
        for i in range(1, self.numNodes + 1):
            station = self.edges[i]
            if station.name == station_name:
                return station
        
        print(f"Station with name '{station_name}' not found.")
        return None
    
    def find_num_station(self, station_name):
        for i in range(1, self.numNodes + 1):
            station = self.edges[i]
            if station.name == station_name:
                return i
        return -1
    

        
    def write_file_header(csvfile):
        if not os.path.isfile(csvfile) or os.path.getsize(csvfile) == 0:
            with open(csvfile, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                header = ['to', 'cost', 'nxt', 'scooters', 'name', 'location']
                writer.writerow(header)

    def write_edges_to_csv(self, csvfile):  
        self.write_file_header(csvfile)

        with open(csvfile, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)

            for i in range(1, self.numNodes + 1):
                item = self.edges[i]

                while item is not None:
                    row = [i, item.to, item.cost]
                    writer.writerow(row)
                    item = item.nxt

    def read_edges_from_csv(self, csvfile):

        scooters = []

        

        with open(csvfile, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                to = int(row[0])
                
                with open('scooters.csv', 'r') as scootersfile:
                    reader_ = csv.reader(scootersfile)
                    next(reader)

                    for row_ in reader_:
                        if row_[1] == to:
                            scooters.append(Scooter(row_[0], row_[1]))
                nxt = int(row[1])
                cost = int(row[2])
                
                self.insert_edge(to, nxt, cost, scooters)
    
 
    
#Funciones que se van a usar para leer y escribir en un archivo



