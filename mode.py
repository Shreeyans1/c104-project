import csv
from collections import Counter

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
d1 = Counter(data1)
mode_range = {"75-85":0,"85-95":0,"95-105":0,"105-115":0,"115-125":0,"125-135":0,"135-145":0,"145-155":0,"155-165":0,"165-175":0}

for h1,o1 in d1.items():
    if 75<float(h1)<85:
        mode_range["75-85"]+=o1
    elif 85<float(h1)<95:
        mode_range["85-95"]+=o1
    elif 95<float(h1)<105:
        mode_range["95-105"]+=o1
    elif 105<float(h1)<115:
        mode_range["105-115"]+=o1
    elif 115<float(h1)<125:
        mode_range["115-125"]+=o1
    elif 125<float(h1)<135:
        mode_range["125-135"]+=o1
    elif 135<float(h1)<145:
        mode_range["135-145"]+=o1
    elif 145<float(h1)<155:
        mode_range["145-155"]+=o1
    elif 155<float(h1)<165:
        mode_range["155-165"]+=o1
    elif 165<float(h1)<175:
        mode_range["165-175"]+=o1

mrange,moccurance = 0,0
for range,o1 in mode_range.items():
    if o1>moccurance:
        mrange,moccurance = [int(range.split("-")[0]),int(range.split("-")[1])],o1

mode = float((mrange[0]+mrange[1])/2)
print(mode)