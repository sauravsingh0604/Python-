
for x in range(2,100,1):

    fact=0
    i=2

    while(i<=x/2):
    
        if(x%i==0):
            fact+=1
            break
        i+=1 

    if(fact==1):
        print('',end='')
       
    else:
        print(x,end=' ')

