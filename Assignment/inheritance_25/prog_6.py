"""
Write a python script to create a Calculator 2.0 class with 2 methods for multiplication
and division of 2 values and inherit it from the Calculator class
"""




class calculator_2_0:

    def __init__(self):
        self.m=2
        self.d=0

    def multi(self):
        return self.m*self.d
    
    def div(self):
        try:
            return self.m/self.d
        except Exception:
            print("please enter correct input")



class calculator(calculator_2_0):


    def __init__(self):
        super().__init__()
        self.a=2
        self.b=4

    def adding(self):
        return (self.a+self.b)
    
    def subtracting(self):
        if self.a>self.b:
            return self.a-self.b
        else:
            return self.b-self.a



cal=calculator()

print(cal.adding())
print(cal.subtracting())

print(cal.multi())
print(cal.div())







