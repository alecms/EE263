import numpy

def xtPlus1(x, A, b):
    x_t_plus_1 = numpy.dot(A,x) + b
    return x_t_plus_1
