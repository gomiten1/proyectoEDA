class Client:
    def __init__(self, id, name, address, phone, mail, card_data):
        self.id = id
        self.name = name
        self.address = address
        self.phone = phone
        self.mail = mail
        self.card_data = card_data
        
    def __str__(self) -> str:
        return ("ID: " + str(self.id) + ", name: " + self.name + ", address: " + self.address
                + ", phone: " + self.phone + ", mail: " + self.mail + ", card: " + self.card_data)
                    
        