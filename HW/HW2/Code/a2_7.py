import numpy as np

transition_matrix = np.matrix('0.9,0,0.1,0; 0.8,0,0.2,0; 0,0.5,0,0.5; 0,0.1,0,0.9')
transition_matrix

def steady_state_power (transition_matrix):
    return np.linalg.matrix_power(transition_matrix, 200)

a = steady_state_power(transition_matrix)
steady_state_values = a[0]
print("Power iteration >X> [{:.3f}, {:.3f}, {:.3f}, {:.3f}]".format(steady_state_values[0,0],steady_state_values[0,1],steady_state_values[0,2],steady_state_values[0,3]))
snowOnThirdDay = steady_state_values[0,0]*transition_matrix[0,2] + steady_state_values[0,1]*transition_matrix[2,1]+steady_state_values[0,2]*transition_matrix[1,2] + transition_matrix[3,3]*steady_state_values[0,3]
print("Part b) probability that it will be snowy 3 days from today: {:.3f}".format(snowOnThirdDay))