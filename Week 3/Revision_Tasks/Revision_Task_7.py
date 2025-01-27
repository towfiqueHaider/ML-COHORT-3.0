'''
write a program to 
accept marks of 6 students and 
display them in a sorted manner and
find out their average
'''

marks = []

for i in range(0,6):
    newElement = str(input(f"Enter marks of {i+1}th student: "))
    marks.append(newElement)
marks.sort()
print(marks)