'''
2. Write a Python script to create a list of first N odd natural numbers.


'''

   
n=int(input("Enter Natural number :"))
list=[]
for x in range(1,n*2+1,2):
     list.append(x)

print(" N natural number : ",list) 