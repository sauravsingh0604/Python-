"""
Write a python script to update 2nd Question, add a class variable (platform) and
create a classmethod to access it.
"""


class profile:

    plateform='CSBS'

    def __init__(self):
        self.name="ankit"
        self.email="ankitpatel9229@gmail.com"
        self.age=19

    def get_profile(self):
        print(self.name)
        print(self.email)
        print(self.age)

    def display(cls):
        return cls.plateform


obj=profile()
obj.get_profile()
print(obj.display())