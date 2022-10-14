#. Write a python program to create a function that takes a number as a parameter and checks if the number is prime or not.

def f1(x):
    fact=0
    i=2
    if x==0 or x==1:
        print(x,"is not prime")
    
    while(x/2==0):
        if(x%i==0):
           print(x,"is not prime")
        i+=i
    else:
          print(x,"is prime")

x=int(input("Enter a numbeer"))
f1(x)