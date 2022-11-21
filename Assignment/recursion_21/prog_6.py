"""
Write a recursive python function to print first N even natural numbers in reverse
order
"""
def printN_even(n):

     if n>0:
        
        if n%2==0:
            print(n)
        printN_even(n-1)

num=int(input("Enter a number : "))
n=num*2
printN_even(n)