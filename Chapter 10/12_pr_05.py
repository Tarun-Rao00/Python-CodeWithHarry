class Train:
    def __init__(self, name, seats, fare):
        self.name = name
        self.seats = seats
        self.fare = fare
    
    def getStatus(self):
        print(f"The name of the train is: {self.name}")
        print(f"The number of seats available in the the train is: {self.seats}")
    
    def getFareInfo(self):
        print(f"The price of ticket is: Rs. {self.fare} /-")


RajdhaniExp = Train("Rajdhani Express - (14026)", 300, 74.5)
RajdhaniExp.getStatus()
RajdhaniExp.getFareInfo()