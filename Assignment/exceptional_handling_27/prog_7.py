"""
Write a python script to add a finally block for the above script
"""



try:
    print("file open")
    
    print("'+'  Addition")
    print("'-'  Substraction")
    print("'*'  Multiplication")
    print("'/'  Division")
    op=input("choose a operation : ")
    
        
    
    if op=='+' or op=='-' or op=='*' or op=='/':
     match op:
        case '+':
            a=int(input("Enter the value of  a : "))
            b=int(input("Enter the value of b : "))
            c=a+b
            
           
        
        case '-':
            a=int(input("Enter the value of  a : "))
            b=int(input("Enter the value of b : "))
            
            c=a-b
            

        case '*':
            a=int(input("Enter the value of  a : "))
            b=int(input("Enter the value of b : "))
            c=a*b
            

        case '/':
            a=int(input("Enter the value of  a : "))
            b=int(input("Enter the value of b : "))
            c=a/b
    else:
        raise NameError()        

except ZeroDivisionError:
    print("you can not divide with zero")
except ValueError:
    print("you have entered invalid value")
except NameError:
    print("please choose correct operation ")
else: 
    print(c)
finally:
    print("file close")

        

