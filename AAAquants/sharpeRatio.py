# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 23:59:35 2020

@author: Diego
"""


import numpy as np 
import pandas as pd 
import pandas_datareader as web
import matplotlib.pyplot as plt 

from datetime import datetime, timedelta

df = web.get_data_yahoo('AMZN')['Adj Close']

#this variable is used for checking to see if we are in a position or not
in_position = 0

#this makes the hold position
hold_period = timedelta(60)

#this is for how long we have to wait
wait = 0

#this stuff is for the P/L, puts them into a list

#this will keep how much money we have made with each trade
pnl = []

#this will keep track if we were in or not
pos = []


time_in_trade = []

#go through all of the dates
for date in df.index:

    #if position is set to 0 which it is and wait is set to 2 which means 2 days have ellipsed then 
    if in_position == 0 and wait == 2:

        #mark the entry price as the price for that date
        entry_price = df[date]

        #market the date of transaction
        open_time = date

        #mark that we are in a position which means that we don't want to get into another one
        in_position = 1

    #this is for when we are in the position and we want to get out. The hold period is 60 days so if 60 days have elapsed we want to sell
    elif in_position == 1 and date - open_time >= hold_period:

        #the profit is the market rate (today's price) minus the price we paid for it
        p = df[date] - entry_price

        #then we want to put that value into the pnl list
        pnl.append(p)

        #this means that we want to tell the program that we sold
        in_position = 0

    #if we are not in a position but enough time hasn't elapsed for us to buy 
    elif in_position == 0 and wait < 2:

        #increase the wait time by one
        wait += 1
    
    pos.append(in_position)


pos1 = [0] + pos 
daily_ret = df.pct_change()*pos1[:-1]