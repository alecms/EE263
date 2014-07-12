import numpy
import power_control
import discrete_time

def findPhistory(number_of_epochs):
    
    reload(power_control)
    reload(discrete_time)
            
    A = power_control.findA()
    b = power_control.findB()
    
    p = numpy.zeros((power_control.n, 1))
    
    epoch_range = range(number_of_epochs)
    
    p_history = numpy.zeros(shape=(power_control.n,number_of_epochs))
    
    for i in epoch_range:
        p_history[:, i] = p.T
        p = discrete_time.xtPlus1(p, A, b)                
    return p_history

def findSinrHistory(p_history):
    
    reload(power_control)
    
    number_of_epochs = p_history.shape[1]
    epoch_range = range(number_of_epochs)
    
    sinr_history = numpy.zeros(shape=(power_control.n,number_of_epochs))
    
    for i in epoch_range:
        p = p_history[:, i]
        sinr = power_control.findSinr(p)
        sinr_history[:, i] = sinr.T
        
    return  sinr_history
    
number_of_epochs = 10
epoch_range = range(number_of_epochs)

phistory = findPhistory(number_of_epochs)
sinr_history = findSinrHistory(phistory)
print sinr_history

p = phistory[:,1]
import power_control
reload(power_control)
print power_control.findInterference(p,0)

import matplotlib

matplotlib.pyplot.plot(phistory[0,:], label= 'p0')
matplotlib.pyplot.plot(phistory[1,:], label= 'p1')
matplotlib.pyplot.plot(phistory[2,:], label= 'p2')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()


matplotlib.pyplot.plot(sinr_history[0,:], label= 'S_0')
matplotlib.pyplot.plot(sinr_history[1,:], label= 'S_1')
matplotlib.pyplot.plot(sinr_history[2,:], label= 'S_2')
matplotlib.pyplot.legend()

    
    
    