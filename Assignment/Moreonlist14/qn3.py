'''
3. Write a Python script to create a list of first N even natural numbers.

'''

n=int(input("Enter Natural number :"))
list=[]
for x in range(2,n*2+1,2):
     list.append(x)

print(" N natural number : ",list) 
