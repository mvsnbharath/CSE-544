import pandas as pd
import numpy as np


def variance(arr):
    mean = 0
    square_sum = 0
    n = len(arr)
    for i in arr:
        mean = mean + i
        square_sum = square_sum + (i * i)

    mean = mean / n
    return square_sum / n - (mean * mean)


df1 = pd.read_csv('q6_X.dat', sep=",", header=None)
X = df1[0].tolist()

df2 = pd.read_csv('q6_Y.dat', sep=",", header=None)
Y = df2[0].tolist()

D = [a_i - b_i for a_i, b_i in zip(X, Y)]
d = np.mean(X) - np.mean(Y)
t = np.abs(d / (np.sqrt(variance(D)) / np.sqrt(len(D))))
print(round(t, 3))
