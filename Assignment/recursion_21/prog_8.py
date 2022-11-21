"""
Write a recursive python function to print cubes of first N natural numbers
"""
def cube_num(n):
    if n>0:
        cube_num(n-1)
        print(n**3)

n=int(input("Enter a number : "))
cube_num(n)