"""
Write a recursive python function to print first N natural numbers.

"""

def printN(n):

    if n==0:
        pass
    else:
        printN(n-1)
        print(n)

printN(3)