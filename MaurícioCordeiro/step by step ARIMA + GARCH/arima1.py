import numpy as np
import pandas as pd
import yfinance as yf

#reading the code that has the forecasts and then they rename the dataset as date and signal
forecasts = pd.read_csv("sp500_forecasts_new.csv", header = None).rename(columns = {0: 'Date', 1: 'Signal'})

#then we want to reset the index so that it is indexed on date
forecasts.set_index('Date', inplace = True)

#now we want to turn the dates into datetimes
forecasts.index = pd.to_datetime(forecasts.index)

#now we want to pull the S&P 500 index, it looks like we can just pull the maximum history for the S&P 
df = yf.Ticker("^GSPC").history(period = 'max')

#then this chops the datafame into our desired length
df = df[(df.index > "1952-01-03") & (df.index < "2020-12-30")]

#adding signals on
df['Signal'] = forecasts['Signal']


#making the log returns of close price
df['LogRets'] = np.log(df['Close'] / df['Close'].shift(1))

#then we multiply the signal by the log rets
df['StratLogRets'] = df['LogRets'] * df['Signal']

#now we want the signals to get stronger and weaker as we progress through time
df['BuyHold_Log_Returns'] = df['LogRets'].cumsum()

#not sure what this does
df['Strategy_Log_Returns'] = df['StratLogRets'].cumsum()

#exponentiate it out
df['BuyHold_Returns'] = np.exp(df['BuyHold_Log_Returns'])
df['Strategy_Returns'] = np.exp(df['Strategy_Log_Returns'])

plot1 = df[['BuyHold_Returns', 'Strategy_Returns']].plot(figsize = (15,7), logy = True) 

#it won't work cutting the dataframe at the end you need to cut it first and the do the changes
df_new = df[(df.index > "2010-01-01")]
plot2 = df_new[["BuyHold_Returns", "Strategy_Returns"]].plot(figsize = (15,7), logy = True)