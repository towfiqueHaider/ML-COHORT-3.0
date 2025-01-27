"""
3. write a python program to 
find average of 'n' numbers taken from user input
"""

n = int(input("Enter number of input: "))
a = []
sum = 0

for i in range(0,n):
    b = int(input(f"Enter {i+1}th input: "))
    a.append(b)
    sum = sum + a[i]


avg = float(sum/n)

print(avg)




