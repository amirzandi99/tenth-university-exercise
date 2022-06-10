class Auto_t:
    manufacturer = ""
    model = ""
    odometer = 0
    def __init__(self, manufacturer, model, odometer, pd_d, pd_m, pd_y, cp_d, cp_m, cp_y, capacity, reservoir):
        self.manufacturer = manufacturer
        self.model = model
        self.odometer = odometer
        self.dateT = Date_t(pd_d, pd_m, pd_y, cp_d, cp_m, cp_y)
        self.tankT = Tank_t(capacity,reservoir)
    def printAuto(self):
        print(f"manufacturer : {self.manufacturer}")
        print(f"model        : {self.model}")
        print(f"odometer     : {self.odometer}")
    def printAll(self):
        print(f"{self.manufacturer} {self.model} {self.odometer} {self.dateT.pd_d} {self.dateT.pd_m} {self.dateT.pd_y} {self.dateT.cp_d} {self.dateT.cp_m} {self.dateT.cp_y} {self.tankT.capacity} {self.tankT.reservoir}")
# 
class Date_t():
    pd_y = 0 # production date year
    pd_m = 0 # production date month
    pd_d = 0 # production date day
    cp_y = 0 # car purchase year
    cp_m = 0 # car purchase month
    cp_d = 0 # car purchase day
    def __init__(self, pd_d, pd_m, pd_y, cp_d, cp_m, cp_y):
        self.pd_d = pd_d
        self.pd_m = pd_m
        self.pd_y = pd_y
        self.cp_d = cp_d
        self.cp_m = cp_m
        self.cp_y = cp_y
    def printDate(self):
        print(f"productionDate : {self.pd_d}/{self.pd_m}/{self.pd_y}")
        print(f"carPurchase    : {self.cp_d}/{self.cp_m}/{self.cp_y}")
# 
class Tank_t():
    capacity = 0
    reservoir = 0
    def __init__(self, capacity, reservoir):
        self.capacity = capacity
        self.reservoir = reservoir
    def printTank(self):
        print(f"capacity  : {self.capacity}")
        print(f"reservoir : {self.reservoir}")
# 
# 
# 
car1 = Auto_t("Mazda","Navajo",123961,2,20,1993,6,15,1993,19.3,16.7)
car2 = Auto_t("Mercury","sable",99842,1,18,2001,5,30,1991,16,12.5)
car1.printAll()
car2.printAll()