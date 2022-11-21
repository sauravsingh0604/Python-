"""
Write a python script to implemented a nested Try Except block
"""

try:
      a=int(input("Enter the value of a : "))
      b=int(input("Enter the value of b : "))
      try:
         if b==0:
            raise ZeroDivisionError()
         c=a/b
            
      except ZeroDivisionError:
        print("you can not divide number with zero")
      else:
        print(c)



except ValueError:
    print('input must be a integer')


