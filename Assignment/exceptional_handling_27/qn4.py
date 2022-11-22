"""
Write a python script to handle a ValueError
"""




try:
    a=int(input("Enter the value of  a : "))
    b=int(input("Enter the value of b except zero: "))
    c=a/b


except ValueError:
    print("you can not divide number rathar than int")
else:
    print(c)