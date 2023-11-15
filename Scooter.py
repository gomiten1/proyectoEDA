class Scooter:
    def __init__(self, id, origin = None, destination = None, client = None):
        self.id = id
        self.origin = origin
        self.destination = destination
        self.client = client
        
    def __str__(self):
        return "ID: " + str(self.id) + ", in use by: " + self.client.name
         
        