# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 16:11:53 2020

@author: Diego
"""


#I want to see how these sklearn models get made, I think you have to make in space a varaible to hold the model

#these will be for all of the sklearn models we are going to want to import
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR

#make a list to hold all of the models
models = []

#now add all of the models to the list
models.append(('LR', LinearRegression()))
models.append(('NN', MLPRegressor(solver = 'lbfgs')))
models.append(('KNN', KNeighborsRegressor()))
models.append(('SVR', SVR(gamma = 'auto')))

Ntest1 = (('LR', LinearRegression()))