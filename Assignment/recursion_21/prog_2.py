"""
Write a recursive python function to print first N natural numbers in reverse order

"""
def printN_rev(n):
    if n==0:
        pass
    else:
        print(n,end=' ')
        printN_rev(n-1)
    
printN_rev(3)