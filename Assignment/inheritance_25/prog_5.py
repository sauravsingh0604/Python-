"""
Write a python script to create a Calculator class with 2 methods for adding and
subtracting 2 values.

"""




class calculator:


    def __init__(self,a,b):
        self.a=a
        self.b=b

    def adding(self,a,b):
        return (self.a+self.b)
    
    def subtracting(self,a,b):
        if self.a>self.b:
            return self.a-self.b
        else:
            return self.b-self.a



cal=calculator(2,4)
print(cal.a)
print(cal.b)



print("sum is ",cal.adding(cal.a,cal.b))
print("sub is ",cal.subtracting(cal.a,cal.b))

