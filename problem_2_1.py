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
    
    
    