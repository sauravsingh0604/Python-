'''
7. Write a python program to check whether a given number is positive, negative or
zero using match case statement
'''

x=int(input("Enter a number"))

match(x):

    case x if x>0:
        print(x,"Number is Positive")
    case x if x<0:
        print(x,"Number is negatitve")
    case x if x==0:
        print("zero") 