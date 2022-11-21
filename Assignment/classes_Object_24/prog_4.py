
"""
Write a python program to init default values for user object using __init__ method.

"""


from re import A


class user:

    def __init__(self,name,age,Email):
        self.name=name
        self.age=age
        self.Email=Email


obj1=user("ankit",19,"ankitpatel9229@gmail.com")
print(obj1.name)
print(obj1.age)
print(obj1.Email)

    

