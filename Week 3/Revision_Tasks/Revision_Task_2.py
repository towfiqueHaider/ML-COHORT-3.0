"""
2. write a python program to find 
remainder when a number 'x' taken from user 
input is divided by another number 'y' which is also 
taken from user input

"""
def findRemainder(x,y):
    return x % y

x = int(input("Enter x: "))
y = int(input("Enter y: "))

print(findRemainder(x,y))
