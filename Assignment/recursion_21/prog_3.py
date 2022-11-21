"""
Write a recursive python function to print first N odd natural numbers

"""
def printN_odd(n):
    
    if n>0:
        printN_odd(n-1)
        if n%2!=0:
            print(n)

m=int(input("Enter a number : "))
n=m*2
printN_odd(n)

