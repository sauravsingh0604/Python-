"""
Create a generator to produce first n terms of Fibonacci series
"""

from re import A


def fibonacci(n):
    a=0
    b=1
    while n:
        yield a
        a,b=b,a+b
        n-=1
        
        
    
for e in fibonacci(int(input("Enter a number : "))):
    print(e)


