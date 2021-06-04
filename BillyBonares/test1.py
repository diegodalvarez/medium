import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from statsmodels.tsa.seasonal import seasonal_decompose

#read the data
df = pd.read_csv("AirPassengers.csv", index_col = 0)

#change the index to datetime
df.index = pd.to_datetime(df.index)

#drop null values
df.dropna(inplace = True)

#then plot the it
df.plot()
plt.show()

#then we decompose the model
result = seasonal_decompose(df['#Passengers'], model = "multiplicable", period = 12)


#plotting the seasonality
result.seasonal.plot()
plt.show()

#plotting the result
result.trend.plot(title = "result trend")
plt.show()

#we can plot all components at one time
result.plot()

#try an additive model
result_add = seasonal_decompose(df['#Passengers'], model = "additive", period = 12)

result_add.seasonal.plot()
plt.show()

result_add.plot()