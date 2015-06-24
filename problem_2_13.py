import numpy as np

A = [[0, 0, 1, 0, 1], 
    [1, 1, 0, 1, 0],
    [1, 0, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0]]

B = np.linalg.matrix_power(A,6)

C = np.linalg.matrix_power(A,3)

print B

i = 3

print B[i-1]

for i in range (1,6):
    print "Number of combinations of symbol ", i, " = ", np.sum(B[i-1]) * np.sum(C[:, i-1])

