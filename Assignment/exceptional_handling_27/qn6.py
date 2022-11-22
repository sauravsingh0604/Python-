"""
Write a python script to create a calculator with 4 basic operations, and handle a
maximum number of exceptions.
"""
try:
    
    print("'+'  Addition")
    print("'-'  Substraction")
    print("'*'  Multiplication")
    print("'/'  Division")
    op=input("choose a operation : ")

    match op:
        case '+':
            a=int(input("Enter the value of  a : "))
            b=int(input("Enter the value of b : "))
            c=a+b
            print(c)
           
        
        case '-':
            a=int(input("Enter the value of  a : "))
            b=int(input("Enter the value of b : "))
            
            c=a-b
            print(c)

        case '*':
            a=int(input("Enter the value of  a : "))
            b=int(input("Enter the value of b : "))
            c=a*b
            print(c)

        case '/':
            a=int(input("Enter the value of  a : "))
            b=int(input("Enter the value of b : "))
            c=a/b
            print(c)

except ZeroDivisionError:
    print("you can not divide with zero")
except ValueError:
    print("you have entered invalid value")
except Exception:
    print("retry......you have entered invalid input")


        

