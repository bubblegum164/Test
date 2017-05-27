import csv
import statsLib as stat

reader = csv.reader(open("nums.csv", 'rb'))

line =[]

for row in reader:
    line = line + row

ind = 0
for val in line:
    line[ind] = int(val)
    ind = ind + 1

print(line)
print(stat.avg(line))
print(stat.stdev(line))
