import csv

with open('data.csv',newline = '')as f:
    r1 = csv.reader(f)
    data = list(r1)

data.pop(0)
data1 = []
n = len(data)
for i in range(n):
    num = data[i][2]
    data1.append(float(num))

n1 = len(data1)
total = 0

for i in data1:
    total = total+i

mean = total/n1
print(mean)