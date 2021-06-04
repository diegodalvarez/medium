import time
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from tqdm import tqdm
from scipy.stats import zscore
from pandas_datareader import data
from datetime import datetime, timedelta

#function to extract statistics for each stock
def get_key_stats(tgt_website):
 
    # The web page is make up of several html table. By calling read_html function.
    # all the tables are retrieved in dataframe format.
    # Next is to append all the table and transpose it to give a nice one row data.
    df_list = pd.read_html(tgt_website)
    df_statistics = df_list[0]
 
    for df in df_list[1:]:
        df_statistics = df_statistics.append(df)
 
    # Transpose the result to make all data in single row
    return df_statistics.set_index(0).T
        

#function to find the last recent weekday for a given date e.g. Fri if Sat or Sun 

def lastBusDay(enterdate):
    if enterdate.weekday()==6:
        lastBusDay = datetime(year=enterdate.year, month=enterdate.month, day=enterdate.day-2)
    elif enterdate.weekday()==5:
        lastBusDay = datetime(year=enterdate.year, month=enterdate.month, day=enterdate.day-1)
    else:
        lastBusDay = enterdate
    return lastBusDay
        
#Randomly selects a user defined no of stocks based on the variable below from a long list of stocks from SGX,HKSE or S&P500

noOfCounters=30


table=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
df = table[0]
spx_symbols = df['Symbol'].to_list()

total_list = spx_symbols


rand=random.sample(range(len(total_list)), noOfCounters)

symbols=[]
for i in range(0,noOfCounters):
    symbols.append(total_list[rand[i]])

#This part of the script extracts the statistics and the current + 1 year ago adj close price (to calculate stock returns) for the stocks defined in the variable 'symbols'

#Blank dict to 'store' the statistics for each stock
df_statistics = {}

current = datetime.now() - timedelta(1) #current date set a day before as data may not be avail for today

currentMinus1Yr=datetime(year=current.year-1, month=current.month, day=current.day)

prices_current=[]
prices_lastyear=[]
prices_return=[]

for symbol in tqdm(symbols):
    try:
        df_statistics[symbol] = get_key_stats(r'https://finance.yahoo.com/quote/' + symbol + '/key-statistics?p=' + symbol)
        time.sleep(random.randint(1,2)) # used to avoid getting blocked by Yahoo Finance for webscraping - if you are fancy - please feel free to modify this code to use Proxy IPs or rotating Request Headers etc
        
        price_current=round(data.DataReader(symbol, start=lastBusDay(current), end=lastBusDay(current), data_source='yahoo')['Adj Close'][-1],4)
        price_lastyear=round(data.DataReader(symbol, start=lastBusDay(currentMinus1Yr), end=lastBusDay(currentMinus1Yr), data_source='yahoo')['Adj Close'][-1],4)
        price_return=round((price_current/price_lastyear-1)*100,1)
        time.sleep(random.randint(1,2))
        
    except:
        print("Unable To Extract Statistics For ",symbol)
        price_current=np.nan
        price_lastyear=np.nan
        price_return=np.nan
        print("Unable To Extract Prices For ",symbol)
        
    prices_current.append(price_current)
    prices_lastyear.append(price_lastyear)
    prices_return.append(price_return)
    
stockprice_df=pd.DataFrame(zip(prices_current,prices_lastyear,prices_return),\
                           columns=["Adj Close "+lastBusDay(current).strftime('%Y-%m-%d'),\
                                    "Adj Close "+lastBusDay(currentMinus1Yr).strftime('%Y-%m-%d'),"Stock Price Returns"],\
                            index=symbols)