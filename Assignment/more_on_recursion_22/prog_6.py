"""
Write a recursive python function to calculate the factorial of a number.

"""
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

n=int(input("Enter a number : "))
print("factorial of a number %d is "%n,fact(n))