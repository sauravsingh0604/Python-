'''

4. Write a program which takes user’s age and display the category of person. Age
below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -
Experienced, Age above or equal 60 - Senior Citizen.

'''
x=int(input("Enter a user age"))

match(x):

    case x if x<10:
        print("kid")

    case x if x<20:
        print("Teen")
    
    case x if x<40:
        print("young")

    case x if x<60:
        print("Experinced")

    case x if x>=60:
        print("Senior citizen")

    case _:
        print("Error input")




