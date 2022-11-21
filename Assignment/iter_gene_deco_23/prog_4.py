"""
Create a generator to produce squares of first N natural numbers

"""

def sqr_num(n):
    a=1
    while n:
        
        yield a**2
        a+=1
        n-=1

for e in sqr_num(int(input("Enter a number : "))):
    print(e)