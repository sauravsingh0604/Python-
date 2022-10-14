'''
7. Write a python script to count digits in a given number

'''

N=int(input("count digit Number  enter is : "))

count=0

for x in str(N):
    count+=1

print(count,"digit count")