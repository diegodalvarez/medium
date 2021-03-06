# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 14:25:23 2021

@author: Diego
"""

import numpy as np
import scipy.sparse
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#making the bottom boundary
def bottom_boundary_condition(K, T, S_min, r, t):
    
    #we want the bottom side to be all zeros
    return np.zeros(t.shape)

#this is for the top condition
def top_boundary_condition(K, T, S_max, r, t):
    
    #S_max - exp(-r(1-t))K
    return S_max - np.exp(-r(1-t)) * K

#And we want the final boundary condition
def final_boundary_condition(K, T, S_min, r, t):
    
    #that is just the option payout max
    return np.max(S_min - K, 0)

#when we make the ODE we will get V_{t-1} = (1 - \lambda \gamma t)V_t - S_t W_t, so we need a way to get Lambda
def compute_abc(K, T, sigma, r, S, dt, dS):
    
    a = -sigma**2 * S**2 / (2*dS**2) + r*S / (2*dS)
    b = r + sigma**2 * S**2 / (dS**2)
    c = -sigma**2 * S**2 / (2* dS**2) - r*S / (2*dS)
    
    return a,b,c

def compute_lambda(a,b,c):
    
    return scipy.sparse.diags ([a[1:], b, c[:-1]], offsets = [-1, 0, 1])

def compute_W(a, b, c, V0, VM):
    
    M = len(b) + 1
    W = np.zeros(M-1)
    W[0] = a[0] * V0
    W[-1] = c[-1] * VM
    
    return W

def price_call_explicit(K,T,r,sigma,N,M):
    
    dt = T/N
    S_min = 0
    S_max = K * np.exp(8 * sigma * np.sqrt(T))
    dS = (S_max - S_min) / M
    S = np.linspace(S_min, S_max, M+1)
    t = np.linspace(0,T,N+1)
    V = np.zeros((N+1, M+1))
    
    #set the boundary conditions
    V[:,-1] = top_boundary_condition(K,T,S_max,r,t)
    V[:,0] = bottom_boundary_condition(K,T,S_max,r,t)
    V[-1,:] = final_boundary_condition(K,T,S)
    
    a,b,c = compute_abc(K,T,sigma,r,S[1:-1],dt,dS)
    Lambda = compute_lambda(a,b,c)
    identity = scipy.sparse.identity(M-1)
    
    for i in range(N,0, -1):
        
        W = compute_W(a,b,c,V[i,0], V[i,M])
        V[i-1, 1:M] = (identity-Lambda*dt).dot(V[i,1:M]) - W*dt
        
    return V,t,S

test = price_call_explicit(200, 5, 0.05, 3, 10, 5)