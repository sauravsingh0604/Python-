"""
Write a python program to create a School class and 3 instance variables and 1 class
variable.

"""

from asyncore import readwrite


class School:

    school="oxford"  

    def __init__(self):   
        self.location="rewa"
        self.depart="10"
        self.principle="sushma ma'am"

    
obj=School()
print(obj.location)
print(obj.depart)
print(obj.principle)

print(obj.school)