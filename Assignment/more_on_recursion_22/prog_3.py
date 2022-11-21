"""
Write a recursive python function to calculate sum of first N even natural numbers
"""
def sum(n):
    if n==0:
        return 0
    else:
        return 2*n + sum(n-1)

       
n=int(input("Enter a number : "))
print(type(n))
print("sum of odd number is ",sum(n))