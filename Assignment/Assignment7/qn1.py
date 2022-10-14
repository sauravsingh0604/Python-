'''
1. Write a python script to display the number of days in a given month number.
'''

x=int(input("enter month value in numeric format : "))

match x:
    
    case x if x in (1,3,5,7,8,10,12):
         print("31 days")
    case x if x in (4,6,9,11):
         print("30 days")
    
    case 2:
        print("28 or 29 days")
         
    case _:
         print("invalid input month")


