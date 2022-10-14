'''
8. Write a python program to Sort a tuple of tuples by the second item.


'''

tuple = (('a', 21),('b', 37),('c', 11), ('d',29))

print("Orignal List: ", tuple)

def Sort(tuple): 
    return(sorted(tuple, key = lambda a: a[1]))  
 

print("Sorted List: ", Sort(tuple)) 
