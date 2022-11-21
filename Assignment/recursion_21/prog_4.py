"""
Write a recursive python function to print first N odd natural numbers in reverse order
"""
def printN_odd(n):
    
    if n>0:
        
        if n%2!=0:
            print(n)
        printN_odd(n-1)

m=int(input("Enter a number : "))
n=m*2
printN_odd(n)