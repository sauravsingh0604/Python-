"""
Write a python script to update the above Profile class with encapsulation.
"""




class profile:

    def __init__(self):
        self.name="ankit"
        self.email="ankitpatel9229@gmail.com"
        self.age=19

    def get_profile(self):
        print(self.name)
        print(self.email)
        print(self.age)


obj=profile()
obj.get_profile()