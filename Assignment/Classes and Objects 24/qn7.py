# Write a python program to create a Laptop class with 4 attributes (brand, ram, cpu,hdd) and 2 methods (showConfig() to print the values, __init__() to initialize thevalues).


class Laptop:
    def __init__(self,brand,cpu,ram,hdd):
        self.brand=brand
        self.cpu=cpu
        self.ram=ram
        self.hdd=hdd

    def showconfig(self):
        print("Brand",self.brand,"ram :",self.ram,"cpu",self.cpu,"HDD: ",self.hdd)


user1=Laptop("Hp","i7","5","1 TB")

user1.showconfig()