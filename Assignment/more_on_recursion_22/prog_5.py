"""
Write a recursive python function to calculate sum of cubes of first N natural numbers
"""
def sum_sqr(n):
    if n==1:
        return 1
    else:
        return n**3 +sum_sqr(n-1)
    
n=int(input("Enter a number : "))
print("sum is ",sum_sqr(n))