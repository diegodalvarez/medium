import numpy as np
import pandas as pd

#this will be for solving derivatives automatically
from scipy.misc import derivative

#this will be a dataframe that will tsore how quickyl our code arrives to a solution
df = pd.DataFrame(columns = ['iteration', 'x_value', 'function_value'])

#then we start with our initial value of x
xn = 0

#then we make a loop that finds hte x-value for our function value is equal to 0

#then we find an x-value for which our function value is at least as small as our chosen threshold 

#limit of the number of iterations
for n in range(0, 10):
    
    #this makes the function outupt
    fxn = f(xn)
    
    df.loc[len(df)] = [n, x, fxn]