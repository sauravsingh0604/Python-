'''
5. Write a python script to calculate sum of first N even natural numbers

'''

N=int(input("Enter the value of N : "))
sum=0
for x in range(0,N*2+1,2):
      sum=sum+x
print("The sum of first ",N," even natural numbers : ",sum)




