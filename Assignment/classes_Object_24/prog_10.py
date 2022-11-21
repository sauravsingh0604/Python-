"""
Define a class Employee with instance object variables empid, name, salary. Write
__init__() method in the class to initialize instance object variables. Also define
instance methods to input fields and display field values

"""

from unicodedata import name


class employee:

    def __init__(self,empid,name,salary):
        self.empid=empid
        self.name=name
        self.salary=salary

    def show(self):
        print(self.empid,self.name,self.salary)


e=employee(102,"sankar",20000000)
e.show()

        
