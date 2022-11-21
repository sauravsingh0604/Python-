"""
Write a python script to update 2nd Question, change email and age to __email and
__age.
"""

class profile:

    def __init__(self):
        self.name="ankit"
        self.__email="ankitpatel9229@gmail.com"
        self.__age=19

    def get_profile(self):
        return self.name,self.__email,self.__age


obj=profile()
print(obj.get_profile())
