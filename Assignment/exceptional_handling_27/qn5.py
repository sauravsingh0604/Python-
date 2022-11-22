"""
Write a python script to handle multiple Exception in one try
"""
try:
    a=int(input("Enter the value of  a : "))
    b=int(input("Enter the value of b : "))
    c=a/b

except ZeroDivisionError:
    print("you can not divide with zero")
except ValueError:
    print("you can not divide number rathar than int")
except Exception:
    print("retry......you have entered invalid input")
else:
    print(c)