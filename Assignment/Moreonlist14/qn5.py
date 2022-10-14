'''
5. Write a Python script to find the smallest number in a given list of numbers.

'''

n=input("N natural number :")

list=[]
for x in n.split(' '):
     x=int(x)
     list.append(x)


x=min(list)
print(" smallest no is : ",x)




