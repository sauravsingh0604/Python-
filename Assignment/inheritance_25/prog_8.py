"""
Write a python script to create a SmartPhone class by inheriting Calculator 2.0 and
Phone Class.
"""

class calculator_2_0:

    def __init__(self):
        self.m=4
        self.d=2

    def multi(self):
        return self.m*self.d
    
    def div(self):
        try:
            return self.m/self.d
        except Exception:
            print("please enter correct input")


class phone:

    def calling(self):
        print("calling.......")

    def sms(self):
        print("SMS.....")

class smartphone(calculator_2_0,phone):

    pass


obj=smartphone()
obj.calling()

print(obj.multi())
