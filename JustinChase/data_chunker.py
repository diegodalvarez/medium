import math
import numpy as np

def index_marks(nrows, chunk_size):
    return range(chunk_size, math.ceil(nrows / chunk_size) * chunk_size, chunk_size)

def split(dfm, chunk_size):
    
    #we want to index all of the points
    indices = index_marks(dfm.shape[0], chunk_size)
    
    #then split by 
    return np.split(dfm, indices)

def chunk_data(train_data, price_col, time_col, n_prediction_units, windows_size = 15, seasonal_unit = "day", **kwargs):
    
    #these are the columns that are required in Prophet
    ds_col = 'ds'
    y_col = 'y'
    key_map = {time_col: ds_col, price_col : y_col}
    
    #this will make a specific number for the week and the day
    train_data['week'] = train_data[time_col].dt.isocalendar().week
    train_data['day'] = train_data[time_col].dt.isocalendar().day
    
    #this will make a tuple for the week and the year
    train_data['day'] = list(zip(train_data['week'], train_data['day']))
    train_data.drop(columns = ['week'], inplace = True)
    
    #this will get the data and split it
    valid = None
    train = train_data
    
    #conver teh column names in the necessary thing that Prophet needs
    train = train.rename(columns = key_map)
    
    #then we want to group by that tuple that we made
    df = train.groupby(seasonal_unit)
    
    #going to be appending something to the list
    model_data = []
    
    #go through the group names and groupframe in the data that is give
    for group_name, group_frame in df:
        
        #going to fill this chunk data and 
        chunk_data = []
        
        #with each seasonal chunk you then 
    