'''

6. Write a python script which takes a three digit number from the user and displays
only its middle digit

'''

num=int(input("Enter a three digit number : "))
d=int(num/10)
result=d%10
print("the middle digit is ",result)