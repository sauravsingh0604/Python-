"""
Write a python script to create an application like Truecaller where names and
numbers are stored. Truecaller class will have 2 methods (1st to fetch the name of a
number and 2nd to add a new entry).

"""

from unicodedata import name

from numpy import number


class TrueCaller:

   

    def set(self,name,number):
        self.name=name
        self.number=number

    def fetch(self):
        print(self.name)
        print(self.number)
        

obj=TrueCaller()
obj.set("ankit",8770747086)
obj.fetch()