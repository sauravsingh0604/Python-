#5. Write a python program to delete the age property of the user.

class user:
    def __init__(self,age):
        self.age=age
       
    

user2=user(34)
print(user2.age)

user1=user(25)
print(user1.age)


del user1.age
print(user2.age)
print(user1.age)
