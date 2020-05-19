import math
import pandas

colnames = ['i1', 'i2', 'i3', 'i4', 'i5', 'i6', 'i7', 'i8', 'i9', 'i10']
data = pandas.read_csv('q5.csv', names=colnames)


def MAP_decision(pts, p):
    if math.log(p / (1 - p)) >= sum(pts):
        return 0
    else:
        return 1


probs = [0.1, 0.3, 0.5, 0.8]
# print(data)
for p in probs:
    temp = []
    ans = []
    for col in colnames:
        ans.append(MAP_decision(data[col], p))
    print(ans)
