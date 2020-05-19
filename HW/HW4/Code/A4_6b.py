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
    print(mean)
    return square_sum / n - (mean * mean)


df1 = pd.read_csv('q6_X.dat', sep=",", header=None)
X = df1[0].tolist()

df2 = pd.read_csv('q6_Y.dat', sep=",", header=None)
Y = df2[0].tolist()

theta_0 = np.mean(X)
p_mle = np.mean(Y)
n = len(X)

std = (np.sqrt(variance(X) + variance(Y))) / np.sqrt(len(X))

w = np.abs((p_mle - theta_0) / std)
print(round(w, 3))
