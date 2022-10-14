# Write a python program to create a School class and 3 instance variables and 1 class variable.

class school:
    school="KV"

    def __init__(self,roll,name,clss) :
        self.roll=roll
        self.name=name
        self.clss=clss

    def show(self):
        print(self.school,self.roll,self.name,self.clss)

student=school(45 ,"akash" ,9)

student.show()



