"""
Write a python program to create a Laptop class with 4 attributes (brand, ram, cpu,
hdd) and 2 methods (showConfig() to print the values, __init__() to initialize the
values).
"""

class Laptop:
    brand="@dell"

    def __init__(self):
        self.ram=8
        self.cpu="i5"
        self.hdd="1TB"
    
    def showConfig(self):
        print(self.ram,self.cpu,self.hdd)

obj=Laptop()
obj.showConfig()

