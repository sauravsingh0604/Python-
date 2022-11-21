"""
Write a recursive python function to print first N multiples of a given number
"""
def multiple_num(num,multi):

    if multi>0:
        multiple_num(num,multi-1)
        print(num*multi)
    
num=int(input("enter a number : "))
multi=int(input("enter N that print the N multiples of a num "))
multiple_num(num,multi)

