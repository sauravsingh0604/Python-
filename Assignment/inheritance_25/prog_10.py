"""
Write a python script to add the new method in SmartPhone class which accepts
Truecaller object as a parameter and call the fetch method of Truecaller
"""
class TrueCaller:

    def set(self,name,number):
        self.name=name
        self.number=number

    def fetch(self):
        print(self.name)
        print(self.number)

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

    def true(self,obj):
        obj.fetch()



T=TrueCaller()
T.set("ankit",8770747086)

smart=smartphone()
smart.true(T)


