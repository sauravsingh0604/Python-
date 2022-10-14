'''

8. Write a python script to calculate sum of digits of a given number

'''

N=int(input("enter no : "))

sum=0

for x in str(N):
    x=int(x)
    sum+=x

print(sum,"digit count")