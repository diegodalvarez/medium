# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 21:24:49 2020

@author: Diego
"""


import pandas as pd
import datetime as dt
import pandas_datareader as web
import matplotlib.pyplot as plt

start = dt.datetime(2005,1,1)
end = dt.datetime.today()

tickers = ['IVV', 'AGG', 'SHY', 'EEM']
df = pd.DataFrame([web.DataReader(ticker, 'yahoo', start, end)['Adj Close'] for ticker in tickers]).T