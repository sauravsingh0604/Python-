x=5
fact=0
i=2

while(i<=x/2):

    if(x%i==0):
        fact+=1
        break
    i+=1

if(fact==1):
    print(x,"Number is not prime")
else:
    print("No is prime")