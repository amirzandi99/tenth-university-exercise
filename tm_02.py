class Employee:
    fName = ""
    lName = ""
    nCode = ""
    Age = 0
    city = ""
    phone = ""
    workplace = ""
    salary = 0
    def __init__(self, fName, lName, nCode, Age, city, phone, workplace, salary):
        self.setFirstName(fName)
        self.setLastName(lName)
        self.setNationalCode(nCode)
        self.setAge(Age)
        self.setCity(city)
        self.setPhone(phone)
        self.setWorkPlace(workplace)
        self.setSalary(salary)
    # 
    def setFirstName(self, fName):
        self.fName = fName
    def setLastName(self, lName):
        self.lName = lName
    def setNationalCode(self, nCode):
        self.nCode = nCode
    def setAge(self, Age):
        self.Age = Age
    def setCity(self, city):
        self.city = city
    def setPhone(self, phone):
        self.phone = phone
    def setWorkPlace(self, workplace):
        self.workplace = workplace
    def setSalary(self, salary):
        self.salary = salary
    # 
    def getFirstName(self):
        return self.fName
    def getLastName(self):
        return self.lName
    def getNationalCode(self):
        return self.nCode
    def getAge(self):
        return self.Age
    def getCity(self):
        return self.city
    def getPhone(self):
        return self.phone
    def getWorkPlace(self):
        return self.workplace
    def getSalary(self):
        return self.salary
# 
# 
# 
employee = []
employee.append(Employee("hadi","e","51200",40,"shiraz","09127897788","Repairman",5000000))
employee.append(Employee("sina","s","71300",35,"zanjan","09121231133","driver",7000000))
employee.append(Employee("nima","b","14100",30,"tehran","09121112244","accountant",6000000))
employee.append(Employee("reza","m","16111",27,"yazd","09124564466","Guard",4000000))
print("\nbefore sort (city)")
for i in range(len(employee)):
    print(f"  {employee[i].fName} with national code: {employee[i].nCode} from {employee[i].city}")
employee.sort(key = lambda emp: emp.city, reverse = False)
print("\nafter sort (city)")
for i in range(len(employee)):
    print(f"  {employee[i].fName} with national code: {employee[i].nCode} from {employee[i].city}")