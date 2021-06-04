# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 13:30:34 2020

@author: Diego
"""

import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'], 
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']}
                   ,index=[0, 1, 2, 3])

df4 = pd.DataFrame({'B': ['B2', 'B3', 'B6', 'B7'], 
                    'D': ['D2', 'D3', 'D6', 'D7'],
                    'F': ['F2', 'F3', 'F6', 'F7']}, 
                   index=[2, 3, 6, 7])

#if you want tojoing the dataframes wo we only have index orws that are both in A and B you would use inner
result = pd.concat([df1, df4], axis = 1, join = 'inner')

#inner joins so that there are aren't an NaN if you want to complete the whole dataframe there will be NaNs

#to combine the whole dataframe you would use the outer method

outer = pd.concat([df1, df4], axis = 1, join = 'outer')

#if you want to put the index values of df1 then you would use left join

df1.merge(df4, how = 'left')