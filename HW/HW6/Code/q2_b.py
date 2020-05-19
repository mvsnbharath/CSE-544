import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

file = open("./q2_sigma100.dat.txt")
a = 0
b_square = 1
sigma = 100
sigma_square = 10000
i = 1
handles = []


def bayesian_inference(data, i):
    n = len(data)
    sum = np.sum(data)
    square_sum = np.sum(np.square(data))
    sum_avg = sum / n
    se_square = sigma_square / n
    square_sum_avg = square_sum / n
    mean = ((b_square * sum_avg) + (se_square * a)) / (b_square + se_square)
    variance = (b_square * se_square) / (b_square + se_square)
    sigma = math.sqrt(variance)
    print("theta " + str(i) + ": mean, variance - " + str(round(mean, 3)) + ", " + str(round(variance, 3)))
    x = np.linspace(mean - 3 * sigma, mean + 3 * sigma, 1000)
    label, = plt.plot(x, stats.norm.pdf(x, mean, sigma), label="theta-" + str(i))
    handles.append(label)
    return mean, variance


for line in file:
    arr = np.fromstring(line, dtype=float, sep=',')
    a, b_square = bayesian_inference(arr, i)
    i += 1

plt.xlabel('x')
plt.ylabel('Normal distribution')
plt.title("Posterior distributions of theta after each observation")
plt.legend(handles=handles, loc="upper left")
plt.show()
