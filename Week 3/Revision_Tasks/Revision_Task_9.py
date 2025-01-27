'''
write a program to 
take user input of 8 numbers and 
count the unique numbers

'''
a = []
count = 0
for i in range(0,8):
    newElement = int(input(f"Enter {i+1}th number: "))
    a.append(newElement)

print(a)
a.sort()

for j in range(0,7):
    if a[j] == a[j+1]:
        count += 1
    else:
        continue
uniqueNumberCount = 8 - count
print(uniqueNumberCount)
        



