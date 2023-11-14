import csv
from Graph.Station import Station

class Graph:
    edges = []
    grade = []

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
    
    def insert_edge(self, intU, intV, intCost, isDirected, name="", scooters = [], location = ""):
        item = Station()
        item.name = name
        item.scooters = scooters
        item.location = location
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
        vertex_time_plt = 0
        edges_time_plt = 0

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
                    edges_time_plt+=1
                v = v.nxt
            self.edges[u].color = 2
            vertex_time_plt +=1
        return vertex_time_plt,edges_time_plt
        

    def print_color(self):
        i = 1
        print("\nBREADTH FIRST SEARCH: ")
        string = ""
        while i <= self.numNodes:
            if self.edges[i] != None:
                if self.edges[i].color == 0:
                    color = "blank"
                elif self.edges[i].color == 1:
                    color = "gray"
                else:
                    color = "black"
                cont = 0
                tabs = ""
                while cont<self.edges[i].distance:
                    tabs+="\t"
                    cont+=1
                if self.edges[i].distance != -1:
                    string+= tabs + str(i) + ": " + color + "-" + str(self.edges[i].distance) + "\t"
                    string+="\n"
            i+=1
        print(string)
        
    def find_station(self, station_name):
        for i in range(1, self.numNodes + 1):
            station = self.edges[i]
            if station.name == station_name:
                return station
            station = station.nxt
        return None
    
 
    
#Funciones que se van a usar para leer y escribir en un archivo

def serialize_graph(graph, filename):
    with open(filename, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        for vertex, neighbors in graph.vertices.items():
            csv_writer.writerow([vertex] + neighbors)

def deserialize_graph(filename):
    graph = Graph()
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            vertex = row[0]
            neighbors = row[1:]
            for neighbor in neighbors:
                graph.add_edge(vertex, neighbor)
    return graph

'''
# Example usage:
# Serialize the graph to a CSV file
serialize_graph(my_graph, 'graph_file.csv')

# Deserialize the graph from the CSV file
new_graph = deserialize_graph('graph_file.csv')
'''