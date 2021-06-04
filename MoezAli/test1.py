import pandas as pd
import matplotlib.pyplot as plt

from pycaret.regression import *

#reading files
data = pd.read_csv("AirPassengers.csv")

#changing date column to datetime
data['Month'] = pd.to_datetime(data['Month'])

#create a rolling 12 month average
data['MA12'] = data['#Passengers'].rolling(window = 12).mean()

#creating a copy
data['Index'] = data['Month']

#reset index to make the fig
data = data.set_index("Index")

#making the fig
data[['#Passengers', 'MA12']].plot()

#make a series
years = []

series = []
j = 1

#go through all of the months and get the years
for i in range(len(data)):
    
    year = data['Month'][i].year
    years.append(year)
    
    series.append(j)
    j += 1
    
#make that a new column
data['Year'] = years

#add in series
data['Series'] = series

#now split the data into training and testing
train = data[data['Year'] < 1960]
test = data[data['Year'] >= 1960]

#setup the pycaret model
s = setup(data = train, test_data = test, target = '#Passengers', fold_strategy = 'timeseries', numeric_features= ['Year', 'Series'], fold = 3, transform_target = True, session_id = 123)

#this finds the best
best = compare_models(sort = "MAE")