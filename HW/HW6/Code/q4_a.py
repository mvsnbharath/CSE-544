import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.loadtxt('q4.dat')
data = pd.DataFrame(data)
del data[0]

data.columns = ['Y']

data = np.loadtxt('q4.dat')
data = pd.DataFrame(data)
del data[0]

data.columns = ['Y']

time = []
temp = 0
for i in range(len(data)):
    time.append(temp % 1440)
    temp += 1

data['X'] = time

partitions = np.array_split(data, 4)


def compute_B0_B1(X, Y):
    B0 = 0
    B1 = 1

    XY = np.sum(X * Y)
    X_2 = np.sum(X * X)
    X_mean = np.mean(X)
    Y_mean = np.mean(Y)

    B1 = (XY - (len(X) * X_mean * Y_mean)) / (X_2 - (len(X) * X_mean * X_mean))
    B0 = Y_mean - (B1 * X_mean)

    return B0, B1


b0_b1 = []
for i in range(4):
    a, b = compute_B0_B1(partitions[i]['X'], partitions[i]['Y'])
    b0_b1.append((a, b))

for i in range(4):
    temp = b0_b1[i][0] + (b0_b1[i][1] * partitions[i]['X'])
    partitions[i]['YPred'] = temp

    plt.figure(figsize=(8, 8))
    plt.plot(partitions[i]['X'], partitions[i]['Y'], partitions[i]['YPred'])
    plt.ylabel("Nuvmber of VMs'")
    plt.xlabel('Time (In Minutes (divided into slots of 5 mins)')
    plt.title("Number of VM's Vs Time for Partition " + str(i + 1))
    plt.gca().legend(('Y', 'YPred'))
    plt.grid()
    plt.show()

for i in range(4):
    sse = np.sum(np.square(partitions[i]['Y'] - partitions[i]['YPred']))
    print("SSE for Partition " + str(i + 1) + ": " + str(sse))