import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import math

def gen_ecdf(S):

    n = len(S)
    Srt = sorted(S)
    delta = .1
    X = [min(Srt)-delta]
    Y = [0]

    for i in range(0, n):
        X = X + [Srt[i], Srt[i]]
        Y = Y + [Y[len(Y)-1], Y[len(Y)-1]+(1/n)]

    X = X + [max(Srt)+delta]
    Y = Y + [1]

    plt.figure('eCDF')
    plt.figure(figsize=(10,8))
    plt.plot(X, Y ,label='eCDF')
    plt.scatter(Srt, [0]*n, color='red', marker='x', s=100, label='samples')
    plt.xlabel('x', fontsize=18)
    plt.ylabel('Pr[X<=x]', fontsize=18)
    plt.title('eCDF with %d samples. Sample mean = %.2f.' % (n, np.mean(S)), fontsize=18)
    plt.legend(loc="upper left")
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid()
    plt.show()

#2a)
S = [1,3,3,6]
gen_ecdf(S)


#2b)

low = 1
high = 99

S = [np.random.uniform(low, high, 10),np.random.uniform(low, high, 100),np.random.uniform(low, high, 1000)]
for sample in S:
    gen_ecdf(sample)


# Helper Functions for 2c and 2d

def Union(lst1, lst2):
    final_list = lst1 + lst2
    return final_list


# Set of unique values over all_lists
def get_union_of_all(all_lists):
    union_of_all = []
    for each_list in all_lists:
        union_of_all = Union(each_list, union_of_all)

    union_of_all = set(union_of_all)

    union_of_all = list(union_of_all)
    union_of_all = sorted(union_of_all)
    return union_of_all


# Contains duplicates (Used to get all X values)
def union_of_all_without_duplicates(all_lists):
    union_of_all = []
    for each_list in all_lists:
        union_of_all = Union(each_list, union_of_all)

    return union_of_all


def compute_m_random_lists(n):
    low = 1
    high = 99
    all_lists = []

    for i in range(n):
        temp = sorted(np.random.uniform(low, high, 10))
        all_lists.append(temp)
    return all_lists


def get_ecdf_updated(all_lists):
    my_dict = {}
    union_of_all = get_union_of_all(all_lists)
    for e in union_of_all:
        if e not in my_dict:
            my_dict[e] = 0

    num = -1;
    for arr in all_lists:
        x = 0
        prev = 0
        num += 1
        for i in union_of_all:
            count = 0
            while (x < len(arr) and arr[x] == i):
                count += 1
                x += 1
            p = prev + count / len(arr)
            prev = p
            my_dict[i] = (my_dict[i] * num + p) / (num + 1)

    all_X = union_of_all_without_duplicates(all_lists)
    return my_dict, all_X

# 2c)

#My random list
all_lists = [sorted([0.1,3.2,2.3,1.4]),sorted([1.7,3.3,0.8,2.1]),sorted([1.5,2.6,0.8,3.9])]

a,X = get_ecdf_updated(all_lists)
keys = list(a.keys())
keys.insert(0,0)
keys.append(4)

values = list(a.values())
values.insert(0,0)
values.append(1)

plt.figure(figsize=(10,8))
plt.plot(keys, values ,label='eCDF')
plt.scatter(X, [0]*len(X), color='red', marker='x', s=100, label='samples')
plt.xlabel('x')
plt.ylabel('Pr[X<=x]')
plt.title('eCDF')
plt.legend(loc="upper left")

plt.grid()
plt.show()

#2d)

#Input 2d array
k = [10,100,1000]
for m in k:
    all_lists = compute_m_random_lists(m)

    a,X = get_ecdf_updated(all_lists)
    keys = list(a.keys())
    keys.insert(0,0.9)
    keys.append(100)

    values = list(a.values())
    values.insert(0,0)
    values.append(1)

    plt.figure(figsize=(10,8))
    plt.plot(keys, values ,label='eCDF')
    plt.scatter(X, [0]*len(X), color='red', marker='x', s=100, label='samples')
    plt.xlabel('x')
    plt.ylabel('Pr[X<=x]')
    plt.title('eCDF')
    plt.legend(loc="upper left")
    plt.grid()
    plt.show()


def normalCI(X1, X2, Y):
    a1 = np.subtract(1, Y)
    a2 = np.multiply(a1, Y)
    a3 = np.divide(a2, len(Y))
    a4 = np.sqrt(a3)
    a5 = np.multiply(1.96, a4)

    a = np.subtract(Y, a5)
    b = np.add(Y, a5)

    plt.figure(figsize=(10, 8))
    legend1, = plt.plot(X1, a)
    legend2, = plt.plot(X1, b)
    legend3, = plt.plot(X1, Y)
    plt.xlabel('x')
    plt.ylabel('Pr[X<=x]')
    plt.title('eCDF')
    plt.legend(loc="upper left")
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid()
    plt.legend(handles=[legend1, legend2, legend3],
               labels=["Lower limit Normal CI", "Upper limit Normal CI", "Cumulative estimate"])
    plt.show()


# 2e)


data = np.loadtxt("q2.dat")
h = sorted(data)

k = Counter(h)

for key, value in k.items():
    k[key] = k[key] / len(h)

X1 = list(k.keys())
X2 = list(k.values())

ecDf, x = get_ecdf_updated([X1])
Y = list(ecDf.values())




def DKWCI(X1, X2, Y):
    alpha = 0.05
    beta = (math.log(2 / alpha)) / (2 * len(X2))
    beta = math.sqrt(beta)

    a = np.subtract(Y, beta)
    b = np.add(Y, beta)

    plt.figure(figsize=(10, 8))
    legend1, = plt.plot(X1, a)
    legend2, = plt.plot(X1, b)
    legend3, = plt.plot(X1, Y)
    plt.xlabel('x')
    plt.ylabel('Pr[X<=x]')
    plt.title('eCDF')
    plt.legend(loc="upper left")
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid()
    plt.legend(handles=[legend1, legend2, legend3],
               labels=["Lower limit DKW CI", "Upper limit DKW CI", "Cumulative estimate"])
    plt.show()

#2f)
DKWCI(X1,X2,Y)

