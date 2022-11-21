"""
Write a python script to handle the ArithmeticError
"""







try:
    a=int(input("Enter the value of  a : "))
    b=int(input("Enter the value of b : "))
    c=a/b

except ZeroDivisionError:
    print("you can not divide with zero")
else:
    print(c)