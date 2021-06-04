# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 14:58:00 2020

@author: Diego
"""


import pandas as pd
import pandas_datareader as web 
import datetime as dt
 
start = dt.datetime(2000,1,1)
end = dt.datetime.today()

df_DGS1MO = web.DataReader('DGS1MO', 'fred', start, end)
df_DGS3MO = web.DataReader('DGS3MO', 'fred', start, end)
df_DGS6MO = web.DataReader('DGS6MO', 'fred', start, end)
df_DGS1 = web.DataReader('DGS1', 'fred', start, end)
df_DGS2 = web.DataReader('DGS2', 'fred', start, end)
df_DGS3 = web.DataReader('DGS3', 'fred', start, end)
df_DGS5 = web.DataReader('DGS5', 'fred', start, end)
df_DGS7 = web.DataReader('DGS7', 'fred', start, end)
df_DGS10 = web.DataReader('DGS10', 'fred', start, end)
df_DGS20 = web.DataReader('DGS20', 'fred', start, end)
df_DGS30 = web.DataReader('DGS30', 'fred', start, end)

df_DGS1MO.to_excel("df_DGS1MO.xlsx")
df_DGS3MO.to_excel('df_DGS3MO.xlsx')
df_DGS6MO.to_excel('df_DGS6MO.xlsx') 
df_DGS1.to_excel('df_DGS1.xlsx')
df_DGS2.to_excel('df_DGS2.xlsx') 
df_DGS3.to_excel('df_DGS3.xlsx')
df_DGS5.to_excel('df_DGS5.xlsx') 
df_DGS7.to_excel('df_DGS7.xlsx') 
df_DGS10.to_excel('df_DGS10.xlsx')
df_DGS20.to_excel('df_DGS20.xlsx')
df_DGS30.to_excel('df_DGS30.xlsx')