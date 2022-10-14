'''
4. Write a Python script to find the greatest number in a given list of numbers.

'''

n=input("N natural number :")

list=[]
for x in n.split(' '):
     x=int(x)
     list.append(x)


x=max(list)
print(" Greatest no is : ",x)








