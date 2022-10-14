'''
2. Write a python script to calculate sum of squares of first N natural numbers

'''

   
n=int(input("Sum of first n Natural number :"))
sum=0
for x in range(1,n+1):
     x=x*x
     sum+=x

print("sum of first N natural number : ",sum) 