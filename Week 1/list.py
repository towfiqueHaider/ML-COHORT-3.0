#list -task 1
data = [2,3,4,5,6]

data.append(7)
data.remove(3)
# data = [2,4,5,6,7]
sum = 0

for i in range(len(data)):
    sum += data[i]

print(sum) #data = 2+4+5+6+7 = 24 

    

