class Address_t:
    name = ""
    xx = 0
    yy = 0
    zz = 0
    mm = 0
    def __init__(self):
        pass
    def setData(self, xx, yy, zz, mm, name):
        self.setxx(xx)
        self.setyy(yy)
        self.setzz(zz)
        self.setmm(mm)
        self.setName(name)
    # 
    def setName(self, name):
        self.name = name
    def setxx(self, xx):
        self.xx = xx
    def setyy(self, yy):
        self.yy = yy
    def setzz(self, zz):
        self.zz = zz
    def setmm(self, mm):
        self.mm = mm
    # 
    def getName(self):
        return self.name
    def getxx(self):
        return self.xx
    def getyy(self):
        return self.yy
    def getzz(self):
        return self.zz
    def getmm(self):
        return self.mm
    # 
    def printIP(self):
        print(f"name : {self.name}")
        print(f"ip   : {self.xx}.{self.yy}.{self.zz}.{self.mm}\n")
    # 
    def localAddress(self, other):
        if(self.xx == other.xx):
            return 1
        else:
            return 0
    # 
    def printAllIP(self,IPA):
        print("\n\nSample Data")
        for i in range(len(IPA)):
            print(f" {IPA[i].getxx()}.{IPA[i].getyy()}.{IPA[i].getzz()}.{IPA[i].getmm()}\t{IPA[i].getName()}")
        print("")
# 
# 
# 
ip = []
while(True):
    name = str(input("input name : "))
    if(name == "none"):
        tmp = Address_t()
        tmp.setData(0,0,0,0,name)
        ip.append(tmp)
        break
    xx = int(input("input xx   : "))
    yy = int(input("input yy   : "))
    zz = int(input("input zz   : "))
    mm = int(input("input mm   : "))
    tmp = Address_t()
    tmp.setData(xx,yy,zz,mm,name)
    ip.append(tmp)
    print("")
IPS = Address_t()
IPS.printAllIP(ip)
r = ip[0].localAddress(ip[1])
if(r == 1):
    print(f"Machines {ip[0].getName()} and {ip[1].getName()} are on the same local network")
else:
    print(f"Machines {ip[0].getName()} and {ip[1].getName()} are not on the same local network")