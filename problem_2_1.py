import numpy
import power_control
import discrete_time
reload(power_control)
reload(discrete_time)

def findPhistory(number_of_epochs, gamma):
    
    reload(power_control)
    reload(discrete_time)
            
    A = power_control.findA(gamma)
    b = power_control.findB(gamma)
    
    p = 0.0004 * numpy.ones((power_control.n, 1))
    
    epoch_range = range(number_of_epochs)
    
    p_history = numpy.zeros(shape=(power_control.n,number_of_epochs))
    
    for i in epoch_range:
        p_history[:, i] = p.T
        p = discrete_time.xtPlus1(p, A, b)                
    return p_history
    
def findSinrHistory(number_of_epochs, gamma):
    p_history = findPhistory(number_of_epochs, gamma)
    
    epoch_range = range(number_of_epochs)
    
    sinr_history = numpy.zeros(shape=(power_control.n,number_of_epochs))
    
    for i in epoch_range:
        p = p_history[:, i]
        sinr = power_control.findSinr(p)
        sinr_history[:, i] = sinr.T
        
    return  sinr_history
    
number_of_epochs = 50
gamma = 3

alpha_gamma = power_control.alpha * gamma * numpy.ones(number_of_epochs)
phistory = findPhistory(number_of_epochs, gamma)
sinr_history = findSinrHistory(number_of_epochs, gamma)


import matplotlib.pyplot as plt


plt.clf()
plt.cla()
plt.plot(sinr_history[0,:], label= 'S_0')
plt.plot(sinr_history[1,:], label= 'S_1')
plt.plot(sinr_history[2,:], label= 'S_2')
plt.plot(alpha_gamma, label = 'alpha x gamma')
plt.legend()
plt.title('SINR vs. t for gamma = ' + str(gamma))
plt.xlabel('t (epochs)')
plt.ylabel('SINR')
plt.draw()
plt.show()


plt.figure()
plt.plot(phistory[0,:], label= 'p0')
plt.plot(phistory[1,:], label= 'p1')
plt.plot(phistory[2,:], label= 'p2')
plt.legend()
plt.draw()
plt.show()

#def findPhistoryTheOtherWay(number_of_epchs):
#    p = numpy.ones((power_control.n, 1))
#    epoch_range = range(number_of_epochs)
#    
#    p_history = numpy.zeros(shape=(power_control.n,number_of_epochs))
#    
#    for i in epoch_range:
#        p_history[:, i] = p.T
#        p = p * power_control.alpha * power_control.gamma / power_control.findSinr(p)
#    
#    return p_history

    
    
    