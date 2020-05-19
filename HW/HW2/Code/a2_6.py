import random

def rand_walk(init_val, final_high, final_low, prob, N):
    pa = 0
    pb = 0
    for i in range(N):

        currentPrice = init_val

        while 1:
            randomNumberForTheDay = random.uniform(0, 1)
            if randomNumberForTheDay < prob:
                change = 1
            else:
                change = -1

            currentPrice += change

            if currentPrice == final_high:
                pa += 1
                break

            if currentPrice == final_low:
                pb += 1
                break
    a = pa / N
    b = pb / N
    c = (final_high * a + final_low * b)

    return a, b, c


test_cases = [(100, 150, 0, 0.5, 10000), (100, 200, 0, 0.52, 10000), (200, 250, 0, 0.54, 10000)]
for index, test_case in enumerate(test_cases):
    init_val = test_case[0]
    final_high = test_case[1]
    final_low = test_case[2]
    prob = test_case[3]
    N = test_case[4]

    a, b, c = rand_walk(init_val, final_high, final_low, prob, N)
    print("TEST CASE" + str(index) + " >> (" + str(a) + ", " + str(b) + " " + str(c) + ")")
