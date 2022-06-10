class Travel_date:
    destinationName = ""
    distance = 0
    time = 0
    direction = ""
    def __init__(self, destinationName, distance, time, direction):
        self.setDestinationName(destinationName)
        self.setDistance(distance)
        self.setTime(time)
        self.setDirection(direction)
    # 
    def setDestinationName(self, destinationName):
        self.destinationName = destinationName
    def setDistance(self, distance):
        self.distance = distance
    def setTime(self, time):
        self.time = time
    def setDirection(self, direction):
        self.direction = direction
    # 
    def getDestinationName(self):
        return self.destinationName
    def getDistance(self):
        return self.distance
    def getTime(self):
        return self.time
    def getDirection(self):
        return self.direction
    # 
    def printTravel(self):
        print(f"name      : {self.destinationName}")
        print(f"distance  : {self.distance}")
        print(f"time      : {self.time}")
        print(f"direction : {self.direction}")
    # 
    def travelCompare(self, other):
        m = self.distance - other.distance
        print(f"{self.destinationName}\t: {self.distance} km")
        print(f"{other.destinationName}\t: {other.distance} km\n")
        if(m > 0):
            print(f"{self.destinationName} {m} km more from {other.destinationName}")
        elif(m < 0):
            m *= -1
            print(f"{self.destinationName} {m} km less from {other.destinationName}")
        else:
            print(f"distance is equal")
# 
# 
# 
travel_1 = Travel_date("kashan",244,3,"S")
travel_2 = Travel_date("yazd",621,7,"S")
travel_3 = Travel_date("shiraz",930,12,"S")
travel_4 = Travel_date("hamedan",393,5,"E")
travel_1.travelCompare(travel_2)