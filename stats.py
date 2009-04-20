import math

a = float(input("Enter in first data value: "))
arr = []
arr.append(a)

while a != -1:
    a = float(input("Enter in next data value: "))
    if  a != -1:
        arr.append(a)

i = 0.0
sum = 0.0
sq = 0.0
for dat in arr:
    sum = sum + dat
    i = i + 1

avg = sum / i

i = 0.0
for dat in arr:
    sq = sq + ((dat - avg) ** 2)
    i = i + 1

std = math.sqrt(sq / i)
print(arr)
print("avg of values is:" , avg)
print("stdev of values is:", std)
