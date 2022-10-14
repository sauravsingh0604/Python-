'''
4. Write a python script to calculate sum of first N odd natural numbers

'''

N=int(input("Enter the value of N : "))
sum=0

for x in range(1,N*2+1,2):
      sum=sum+x
print("sum of first ",N," odd natural numbers : ",sum)








