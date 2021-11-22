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
data1.sort()

if n1%2 == 0:
    m1 = float(data1[n1//2])
    m2 = float(data1[n1//2-1])
    m = (m1+m2)/2

else:
    m = data1[n1//2]

print(m)