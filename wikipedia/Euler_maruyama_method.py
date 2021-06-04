# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 13:20:19 2021

@author: Diego
"""

import numpy as np
import matplotlib.pyplot as plt

#how many runs we want
num_sims = 5

#beginning
t_init = 3

#end
t_end = 7

#number of grid points
N = 1000

#making the differential
dt = float(t_end - t_init) / N

#initial for y
y_init = 0

#these are points for the Ornsteen-Uhlenbeck process
c_theta = 0.7
c_mu = 1.5
c_sigma = 0.06

#the first part of the Ornstein-Uhlenbeck equation is this mu function
def mu(y,t):
    
    #the operation
    return c_theta * (c_mu - y)

#for the sigma function
def sigma(y,t):
    
    return c_sigma

def dW(delta_t):
    
    #we want a normal distribution with mean 0, and sqrt of the delta time squared
    return np.random.normal(loc = 0.0, scale = np.sqrt(delta_t))

#this splits a range from 3 to 7 into 1000 piececs
ts = np.arange(t_init, t_end + dt, dt)

#then we are going to make a list of 0s to input what we want
ys = np.zeros(N+1)

#define the first one
ys[0] = y_init

#go through the simulations
for _ in range(num_sims):
    
    #go through the size the grid points
    for i in range(1, ts.size):
        
        #want to keep track of time
        t = t_init + (i-1) * dt
        
        #we want to go a step ahead on the y-values
        y = ys[i-1]
        
        #we want to input the values
        ys[i] = y + mu(y,t) * dt + sigma(y, t) * dW(dt)
        
    plt.plot(ts, ys)

plt.xlabel("time (s)")
h = plt.ylabel('y')
plt.show()        
    