'''
write a python program to 
count the number of zeros in a list, 
L=[1,0,0,1,0,0,2,0,3,-5,0,0]
'''

L=[1,0,0,1,0,0,2,0,3,-5,0,0]
count = 0

for i in range(0, len(L)):
    if L[i] == 0:
        count += 1
    else:
        continue

print(count)
