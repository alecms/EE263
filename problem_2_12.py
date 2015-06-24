import numpy as np

A = [[0, 0, 1, 0, 1], 
    [1, 1, 0, 1, 0],
    [1, 0, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0]]
    


A9 = np.linalg.matrix_power(A,9)

print A9

number_length_10_sequences = np.sum(A9)

print "Number of allowable sequences: ", number_length_10_sequences

A = np.ones((5,5))

A9 = np.linalg.matrix_power(A,10)

print A9

number_length_10_sequences = np.sum(A9)

print "Number of allowable sequences: ", number_length_10_sequences