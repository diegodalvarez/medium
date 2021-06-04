from stock import Stock 

#look like accesing attributes of the variable
gspc = Stock('^GSPC')
gspc.start_date = '2000-01-01'
gspc.end_date = '2020-12-31'

#using an method to get the returns
gspc.add_log_return()
gspc.df

#get the log returns
spReturns = gspc.df['LogRets']

#how many days are we looking ahead
windowLength = 500

#this may be counting how many days are left in the dataframe 
foreLength = len(spReturns) - windowLength

windowed_ds = []

#i think what this is doing is putting a series in each value of series, and the series are 500 points
for d in range(foreLength - 1):
    windowed_ds.append(spReturns[d:d + windowLength])
    
#create a forecast dataframe initialized with zeros
forecasts = spReturns.iloc[windowLength].copy() * 0 

