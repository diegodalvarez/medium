# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 13:28:48 2020

@author: Diego
"""


import pandas as pd
import pandas_datareader as web
import datetime as dt

start = dt.datetime(2000,1,1)
end = dt.datetime.today()

df = web.DataReader("AAPL", 'yahoo', start, end)

df_shifted = df.copy()
df_shifted = df['Adj Close'].shift()

#so it looks like it shifts the columns by one value 