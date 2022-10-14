'''
2. Write a menu driven program to perform following operations - Addition, Subtraction,
Multiplication, Division

'''
x=int(input("Enter a number"))
y=int(input("Enter a number"))

print("1 Addition 2.Subtraction 3.Multiplication 4.Division")
z=int(input("Enter a number"))

match(z):
    case 1 :
        print("Addition is",x+y)
    case 2:
        print("Subtraction is",x-y)
    case 3:
        print("Multiplication is",x*y)
       
    case 4:
        print("division is ", x/y)
    