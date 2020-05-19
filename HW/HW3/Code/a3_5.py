import math
import matplotlib.pyplot as plt
import numpy as np

#) 5c
data = np.loadtxt('weather.dat')
a, b = math.floor(min(data)), math.ceil(max(data))

bins = []
count_dict = {}
for i in range(a, b):
    bins.append((i, i + 1))
    count_dict[i] = 0

for val in data:
    x = math.floor(val)
    count_dict[x] = count_dict[x] + 1

x = [key for key in count_dict]
y = [count_dict[key]/len(data) for key in sorted(count_dict)]
xlabels = [str(t) for t in bins]

plt.figure(figsize=(20, 15))
plt.rc('font', size=12)
plt.bar(x, y, width=0.9)

plt.xlabel("bins (i-1,i)")
plt.ylabel("p_i")
plt.title("Histogram estimate h(x)")
# set the labels at the middle of the bars
plt.xticks([x for x in x], xlabels)
plt.show()


#5d)

a, b = math.floor(min(data)), math.ceil(max(data))

count_dict = {}
for i in range(a, b):
    count_dict[i] = 0

for val in data:
    x = math.floor(val)
    count_dict[x] = count_dict[x] + 1

ecdf = []
old = 0
for key in sorted(count_dict):
    p_x = count_dict[key]/len(data)
    ecdf.append(old+p_x)
    old = old+p_x

x = [key for key in count_dict]
y = [count_dict[key]/len(data) for key in sorted(count_dict)]

plt.figure(figsize=(20, 15))
plt.rc('font', size=16)
plt.plot(x, ecdf, linestyle='-')

plt.xlabel("x in bin Bj")
plt.ylabel("F_x")
plt.title("CDF using histogram estimator")
# set the labels at the middle of the bars
plt.xticks([x for x in x])
plt.show()

