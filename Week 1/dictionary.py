#task 3

result = {
    "Math" : 80,
    "Physics" :90,
    "Chemistry" : 70,
    "Biology" : 32
}

result["English"] = 85
sum = 0

for i in result:
    sum += result[i]

avg = float(sum/(len(result)))
print(avg)

