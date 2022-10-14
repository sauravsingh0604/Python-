# Write a python program to create a function that finds a maximum of four numbers.

a,b,c,d=int(input()),int(input()),int(input()),int(input())

def max(a,b,c,d):
    if a>b and a>c and a>d:
        return a
    elif a<b and b>c and b>d: 
        return b
    elif c>d and c>a and c>b:
        return c
    else:

        return d

    
print("Max value is",max(a,b,c,d))