import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

#7a)
D = []
for x in range(0, 800):
    p = np.random.uniform(0, 1)
    if p <= 0.25:
        D.append(np.random.normal(0, 1))
    elif p <= 0.5:
        D.append(np.random.normal(3, 1))
    elif p <= 0.75:
        D.append(np.random.normal(6, 1))
    elif p <= 1:
        D.append(np.random.normal(9, 1))

alphas = np.arange(-5, 10, 0.1)


def kde_estimate(data, h):
    p_pwk_array = []
    alpha_values = np.arange(-5, 10, 0.1)
    for alpha in alpha_values:
        indicator_sum = 0
        for x in data:
            if abs(alpha - x) <= (h / 2):
                indicator_sum += 1
        pwk_val = indicator_sum / (len(data) * h)
        p_pwk_array.append(pwk_val)

    return p_pwk_array, alphas


def true_pdf():
    true_dist = []
    alpha_values = np.arange(-5, 10, 0.1)
    for alpha in alpha_values:
        a = norm(0, 1).pdf(alpha) + norm(3, 1).pdf(alpha) + norm(6, 1).pdf(alpha) + norm(9, 1).pdf(alpha)
        a = a / 4
        true_dist.append(a)
    return true_dist


smoothing_bandwidth = [0.1, 1, 7]
output = []
true_pdf_values = true_pdf()
handles = []

for h in smoothing_bandwidth:
    kde_estimates, alphas = kde_estimate(D, h)
    label, = plt.plot(alphas, kde_estimates, linestyle='-', label="h = " + str(h))
    handles.append(label)

x_alpha = np.arange(-5, 10, 0.1)
plt.xticks([alphas[i] + 0.5 for i in range(0, len(alphas), 10)])
plt.xlabel('alpha')
plt.ylabel('p_kde')
plt.title("kernel density estimation for alpha")
label, = plt.plot(alphas, true_pdf_values, linestyle='-', label = "true distribution")
handles.append(label)
plt.rc('font', size=8)
plt.rc('xtick', labelsize=20)
plt.legend(handles=handles, loc="upper left")
plt.show()


#7b)

def kde_estimate(data, h):
    p_pwk_array = []
    alpha_values = np.arange(-5, 10, 0.1)
    for alpha in alpha_values:
        indicator_sum = 0
        for x in data:
            if abs(alpha - x) <= (h / 2):
                indicator_sum += 1
        pwk_val = indicator_sum / (len(data) * h)
        p_pwk_array.append(pwk_val)

    return p_pwk_array


def true_pdf():
    true_dist = []
    alpha_values = np.arange(-5, 10, 0.1)
    for alpha in alpha_values:
        a = norm(0, 1).pdf(alpha) + norm(3, 1).pdf(alpha) + norm(6, 1).pdf(alpha) + norm(9, 1).pdf(alpha)
        a = a / 4
        true_dist.append(a)
    return true_dist


D = []
data_samples = []
for sample in range(0, 150):
    D = []
    for x in range(0, 800):
        p = np.random.uniform(0, 1)
        if p <= 0.25:
            D.append(np.random.normal(0, 1))
        elif p <= 0.5:
            D.append(np.random.normal(3, 1))
        elif p <= 0.75:
            D.append(np.random.normal(6, 1))
        elif p <= 1:
            D.append(np.random.normal(9, 1))
    data_samples.append(D)

smoothing_bandwidth = [0.01, .1, .3, .6, 1, 3, 7]

# alpha_estimate_lists = []
alpha_kde_estimates = []
alphas = []

expectation_list = []
var_list = []
bias_list = []
mse_list = []
true_dist = true_pdf()
alphas = np.arange(-5, 10, 0.1)

bias_tot_list = []
var_tot_list = []
mse_tot_list = []

print("alphas len - " + str(len(alphas)))
for h in smoothing_bandwidth:
    alpha_estimate_lists = []
    for data in data_samples:
        alpha_kde_estimates = kde_estimate(data, h)
        alpha_estimate_lists.append(alpha_kde_estimates)

    # arranges the list of lists of p_kde(alpha) in numpy array
    alpha_estimate_lists = np.array(alpha_estimate_lists)

    expectation_list = np.sum(alpha_estimate_lists, axis=0)
    expectation_list = expectation_list / len(data_samples)
    diff = np.power(alpha_estimate_lists - expectation_list, 2)
    var_list = np.sum(diff, axis=0)
    var_list = var_list / len(data_samples)
    bias_list = expectation_list - true_dist
    mse_list = var_list + np.power(bias_list, 2)
    bias_tot = np.sum(np.power(bias_list, 2)) / len(alphas)
    var_tot = np.sum(var_list) / len(alphas)
    mse_tot = bias_tot + var_tot
    bias_tot_list.append(bias_tot)
    var_tot_list.append(var_tot)
    mse_tot_list.append(mse_tot)

print("bias tot list - " + str(bias_tot_list))
print("var tot list - " + str(var_tot_list))

plt.plot(smoothing_bandwidth, bias_tot_list, linestyle='--', marker='x')
plt.ylabel("bias_square_tot")
plt.xlabel("smoothing bandwidth(h)")
plt.title("bias_square_tot vs smoothing bandwidth")
plt.show()

plt.plot(smoothing_bandwidth, var_tot_list, linestyle='--', marker='x')
plt.ylabel("var_tot")
plt.xlabel("smoothing bandwidth(h)")
plt.title("var_tot vs smoothing bandwidth")
plt.show()

optimal_h_index = np.argmin(mse_tot_list)
print("Optimal h value - ", smoothing_bandwidth[optimal_h_index])
