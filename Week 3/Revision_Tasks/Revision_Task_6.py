'''
write a program to 
store seven fruits in a list entered by the user
'''
a = []

for i in range(0,7):
    b = str(input(f"Enter {i+1}th fruit name: "))
    a.append(b)

print(a)