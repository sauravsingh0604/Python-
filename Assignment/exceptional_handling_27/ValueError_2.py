"""
Write a python script to create a ValueError
"""

a=20
b=int(input("Enter the value of b  : "))
# if you enter any other value rather than int then you will get ValueError
# for example if you enter str type , complex type .......then you will get ValueError

c=a/b
print(c)