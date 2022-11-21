"""
Write a recursive python function to print squares of first N natural numbers
"""
def sqrnum(n):
    if n>0:
        sqrnum(n-1)
        print(n**2)

n=int(input("Enter a number : "))
sqrnum(n)