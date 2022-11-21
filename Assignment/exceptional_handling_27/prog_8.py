"""
Write a python script to implement try except and else block for division

"""



try:
      a=int(input("Enter the value of a : "))
      b=int(input("Enter the value of b : "))
      c=a/b

except ZeroDivisionError:
    print("you can not divide number with zero")

else:
    print(c)

