import csv
import itertools
import math

with open('acceleration_normal.txt', mode='r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    data = list(reader)

accel = list(itertools.chain.from_iterable(data))
accel = list(map(float, accel))
# print(accel)


with open('model_uniform.txt', mode='r', encoding='utf-8-sig') as f1:
    reader1 = csv.reader(f1)
    data1 = list(reader1)

model = list(itertools.chain.from_iterable(data1))
model = list(map(float, model))
# print(model)

with open('mpg_exponential.txt', mode='r', encoding='utf-8-sig') as f2:
    reader2 = csv.reader(f2)
    data2 = list(reader2)

mpg = list(itertools.chain.from_iterable(data2))
mpg = list(map(float, mpg))

# MME
# normal_distribution
est_mean = sum(accel) / len(accel)
count = 0
for i in accel:
    count = count + (i - est_mean) * (i - est_mean)

# uniform_distribution

mean = sum(model) / len(model)
count1 = 0
for i in model:
    count1 = count1 + i * i
S = math.sqrt((count1 / len(model)) - (mean * mean))

# MME
# Normal Distribution
print("MME normal_mean: ", round(est_mean, 3))
print("MME normal_variance: ", round(count / len(accel), 3))

# Uniform distribution
print("MME a estimate: ", round(mean - math.sqrt(3) * S, 3))
print("MME b estimate: ", round(mean + math.sqrt(3) * S, 3))

# Exponential_distribution
print("MME lambda estimate: ", round(len(mpg) / sum(mpg), 3))