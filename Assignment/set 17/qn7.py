'''
7. Write a python program to copy elements 4 and 5 from the following tuple into a new tuple. tuple1=(1,2,3,4,5,6)
'''
tuple1=(1,2,3,4,5,6)

x=slice(3,4,1)
tuple2=tuple1(x)
print(tuple2)