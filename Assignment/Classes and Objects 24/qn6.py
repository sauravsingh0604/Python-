# Write a python program to create 3 user objects and find the youngest of all

class user:

    def __init__(self,age):
        self.age=age

    def compare(self,p,q):
        if self.age > p.age:
            if self.age > q.age:
                print(self.age, "is youngest ")
            else:
                 print(q.age, "is youngest ")
        else:
            if q.age > p.age:
                print(q.age, "is youngest ")
            else:
                 print(p.age, "is youngest ")
        

user1=user(23)

user2=user(34)
user3=user(23)

user1.compare(user2,user3)