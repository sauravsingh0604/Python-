"""
Write a recursive python function to calculate sum of first N natural numbers
"""




def printN(n):
        if n==1:
            return 1
        return n+printN(n-1)

n=int(input("Enter a number : "))
result=printN(n)
print("sum of %d natural number is "%n,result)
