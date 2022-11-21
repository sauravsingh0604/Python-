"""
 Create a generator to produce first n odd natural numbers
"""

def printN_odd(n):
    a=1
    while n:
        yield a
        a+=2
        n-=1

        
for e in printN_odd(int(input("Enter a number : "))):
    print(e)