class Scooter:
    def __init__(self, id, origin = None, destiny = None, client = None):
        self.id = id
        self.origin = origin
        self.destiny = destiny
        self.client = client
        
    def __str__(self):
        return "ID: " + str(self.id) + ", in use by: " + self.client.name
         
        