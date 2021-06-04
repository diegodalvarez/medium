import re
import requests
import numpy as np
import pandas as pd
import yfinance as yf

from bs4 import BeautifulSoup
from googlesearch import search

#problem with tld


#this will computer 1yr performance
def calc_1yr_returns(stock):
    
    tick = yf.Ticker(stock)
    df = tick.history('1y')
    ret = round(100 * ((df['Close'].iloc - df['Close'].iloc[0]) / df['Close'].iloc[0]), 2)
    
    return ret

#calculate cumulative returns
def cumulative_returns(stock):
    
    tick = yf.Ticker(stock)
    df = tick.history('3y')
    df = df[['Close']]
    df['ret'] = df['Close'].pct_change()
    df.dropna(inplace = True)
    df = df[['ret']]
    cumula_ret = (1 + df).cumprod() - 1
    
    return round(100 * cumula_ret['ret'].iloc[-1], 2)

'''
def scrape_web(search_txt):
    
    #keep track of tickers
    symbol_list = []
    
    #keep track of results
    google_res = []
    
    #not sure what this is but something to do with google search
    for l in search(search_txt, tld="co.in", num = 10, stop = 10, pause = 2):
        google_res.append(l)
        
    #something to do with google's response
    for res in google_res:
        
        req = requests.get(res)
        req = req.content
        soup = BeautifulSoup(req, 'lxml')
        bodies = soup.find_all('p')
        
        for body in bodies:
            match = re.search('[A-Z]+', body.text)
            
            if match != None:
                
                txt = match.group()
                print(f'Match: {txt}')
                symbol_list.append(txt)
                
        clean_list = [i.strip(":") for i in symbol_list]
        clean_list.append('SPY')
        return clean_list
'''

def scrape_web(search_txt):
    symbol_list = []
    google_res = []

    for l in search(search_txt, tld="co.in", num=10, stop=10, pause=2):
        google_res.append(l)
    
    for res in google_res:
        req = requests.get(res)
        req = req.content
        soup = BeautifulSoup(req, 'lxml')
        bodies = soup.find_all('p')
        for body in bodies:
            match = re.search(':[A-Z]+', body.text)
            if match != None:
                txt = match.group()
                print(f'Match: {txt}')
                symbol_list.append(txt)
    
    clean_list =[i.strip(':') for i in symbol_list]
    clean_list.append('SPY')
    return clean_list

def create_file(clean_list):
    
    #this looks like it is going to compare 
    rets = map(calc_1yr_returns, clean_list)
    rets_df = pd.DataFrame(rets, columns = ['SPY'].values[0][0])
    sp_ret = rets_df.loc[rets_df.index == 'SPY'].values[0][0]
    rets_df['beat S&P 1yr'] = np.where(rets_df['1yr_return'] > sp_ret, "Yes", "No")
    
    cum_rets = map(cumulative_returns, clean_list)
    cum_rets_df = pd.DataFrame(cum_rets, columns = ['3yr_cumulative_ret'], index = clean_list)
    sp_ret2 = cum_rets.df.loc[cum_rets_df.index == "SPY"].values[0][0]
    cum_rets_df['beat S&P 3yr'] = np.where(cum_rets_df['3yr_cumulative_ret'] > sp_ret2, "Yes", "No")
    
    final_df = pd.merge(rets_df, cum_rets_df, left_index = True, right_index = True)
    final_df = final_df[['1yr_return', '3yr_cumulative_ret', 'beat S&P 1yr', 'beat S&P 3yr']]
    final_df.drop_duplicate(inplace = True)
    final_df.to_excel("Motley Fool Picks 2021.xlsx")
    print("file crated")
    
symbol_list = scrape_web("Top 3 growth stocks Motley Fool")
create_file(symbol_list)