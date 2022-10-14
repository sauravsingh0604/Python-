'''
5. Write a python program to check if all items in the tuple are the same.

'''

t1=4,4,4,4,4,4


for i in range(0,len(t1),1):
      if t1[0]!=t1[i]:
          print("not equal")
          break
else:
    print("equal")