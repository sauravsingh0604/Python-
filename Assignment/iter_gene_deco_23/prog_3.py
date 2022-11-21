"""
Create a generator to produce first n even natural numbers
"""

def printN_even(n):
    a=2

    while n:
        yield a
        a+=2
        n-=1

for e in printN_even(int(input("Enter a number : "))):
    print(e)