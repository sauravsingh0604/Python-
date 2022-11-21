"""
WRT 7th Question, create 3 Laptop objects and add them to the list in the sorted
order based on the ram size.

"""





class Laptop:
    brand="@dell"

    def __init__(self,ram):
        self.ram=ram
        self.cpu="i5"
        self.hdd="1TB"
    
    def showConfig(self):
        print(self.ram,self.cpu,self.hdd)

    @staticmethod
    def sorted1():
        l1=[[int(obj1.ram),obj1.cpu,obj1.hdd],[int(obj2.ram),obj1.cpu,obj1.hdd],[int(obj3.ram),obj1.cpu,obj1.hdd]]
        # print(sorted(l1))
        l1.sort()
        print(l1)
            


obj1=Laptop("16")
obj1.showConfig()


obj2=Laptop("4")
obj2.showConfig()



obj3=Laptop("9")
obj3.showConfig()


Laptop.sorted1()




