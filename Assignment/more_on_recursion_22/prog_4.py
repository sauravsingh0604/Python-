"""
Write a recursive python function to calculate sum of squares of first N natural
numbers

"""
def sum_sqr(n):
    if n==1:
        return 1
    else:
        return n**2 +sum_sqr(n-1)
    
n=int(input("Enter a number : "))
print("sum is ",sum_sqr(n))





