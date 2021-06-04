import datetime as dt
import yfinance as yf

from financial_data import *

#dates
end_date = dt.datetime.today()
start_date = end_date - dt.timedelta(days = (3 * 365) + 1)

#tickers
portfolio_tickers = ['CLX', 'TJX', 'MSFT', 'F', 'MDT', 'LUV', 'CMA', 'NVDA', 'SYY', 'HIG']

#getting & plotting data
my_portfolio = FinancialData(tickers = portfolio_tickers, cols = ['Adj Close','Volume'], start = start_date, end = end_date)
my_portfolio.plot_data(figsize=(20,10),fontsize=15)

#returns
port_returns = my_portfolio.get_returns(plot=True,subplots=True,figsize=(10,20),kind='hist',bins=100)
port_returns = my_portfolio.get_returns(plot=True,subplots=True,figsize=(10,20))

#comparing it to S&P 