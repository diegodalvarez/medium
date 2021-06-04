import numpy as np

from scipy.ndimage.interpolation import shiftdef

#making a function 
def auto_correlation(Data, first_data, second_data, shift_degree, loockback, where):
    
    new_array = shift(Data[:, first_data], shift_degree, cval = 0)
    new_array = np.reshape(new_array, (-1, 1))