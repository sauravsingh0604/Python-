"""
Write a python script to raise a ValueError.
"""

try:
      a=int(input("Enter the value of a : "))
      b=int(input("Enter the value of b : "))
      if a==str or a==float or a==complex:
        raise ValueError()
      c=a/b

except ZeroDivisionError:
    print("you can not divide number with zero")
except ValueError:
    print('invalid computation')

else:
    print(c)