# define constants
import numpy

G = numpy.array([[1, .2, .1], [.1, 2, .1], [.3, .1, 3]])

gamma = 4.7
alpha = 1.2
sigma = 0.01
n = 3

def findA():
    A = numpy.zeros(shape=(n,n))
    for (i,j), value in numpy.ndenumerate(G):
        if i != j:
            A[i,j] = G[i,j] / G[i,i]
        else:
            A[i,j] = 0
    return A

def findB():
    b = numpy.zeros(shape=(n,1))
    for i in range(n):
        b[i] = alpha * gamma / G[i, i]
    return b

def findInterference(p,i):
    interference = 0;
    for j in range(n):
        if j != i:
            interference += G[i,j] * p[j]
    
    return interference
    

def findSinr(p):
    sinr = numpy.zeros(shape=(n,1))
    for i in range(n):
        interference = findInterference(p,i)
        print interference
        
        sinr[i] = G[i, i] * p[i] / (sigma + interference)
    
    return sinr