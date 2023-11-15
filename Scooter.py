class Scooter:
    def __init__(self, id, origin = None, destination = None, client = None, cost = 0):
        self.id = id
        self.origin = origin
        self.destination = destination
        self.client = client
        self.cost = cost
        
    def __str__(self):
        string =  "ID: " + str(self.id)
        if self.origin:
            string+= ", origin: " + self.origin.name
        if self.destination:
            string+= ", intended destination: " + self.destination.name
        if self.client:
            string += ", client: " + self.client.name
        return string
         
        