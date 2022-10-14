# 10. Define a class Employee with instance object variables empid, name, salary. Write __init__() method in the class to initialize instance object variables. Also define instance methods to input fields and display field values


class employee:

    def __init__(self):

        self.empid=""
        self.name=""
        self.salary=""
       
    def input(self):

        self.empid=input("Enter empid ")
        self.name=input("enter name ")
        self.salary=input("enter salary ")

    def show(self):

        print(self.empid,self.name,self.salary)

emp1=employee()


emp1.input()
emp1.show()
