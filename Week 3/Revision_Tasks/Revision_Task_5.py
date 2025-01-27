'''
write a program to 
detect if there are double spaces in a string and 
replace the double space with a single space

'''

my_str = "Hello  World"

if my_str.find("  ") == -1:
    print("There are no double spaces")
else:
    print("There are double spaces int the string")
    y = my_str.replace("  ", " ")
    print(y)