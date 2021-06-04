import numpy as np
import pandas as pd
import datetime as dt
import yfinance as yf
import streamlit as st

from ta.trend import MACD
from ta.momentum import RSIIndicator
from ta.volatility import BollingerBands

#this creates a sidebar
option = st.sidebar.selectbox("Select one symbol", ('AAPL', 'MSFT', 'SPY', 'WMT'))

#making dates
today = dt.date.today()
before = today - dt.timedelta(days = 700)

#put that into the
start_date = st.sidebar.date_input('Start date', before)
end_date = st.sidebar.date_input('End date', today)

#if the start_date is less than the end date
if start_date < end_date:
    
    #then it will work
    st.sidebar.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
    
#this is meant for when it doesn't work
else:
    
    #give an error
    st.sidebar.error("Error: End date must fall after the start date")
    
#getting the data, we can pass option through because that is waht they are going to select
df = yf.download(option, start = start_date, end = end_date, progress = False)

#now we ware going to make the bollingerband, this looks like we need to make a variable BollingerBand variable and pass
#through the dataframe
indicator_bb = BollingerBands(df['Close'])

#make the
bb = df

#making the upper or lower bolling band
bb['bb_h'] = indicator_bb.bollinger_hband()
bb['bb_l'] = indicator_bb.bollinger_lband()

#then making the bollinger band dataframe
bb = bb[['Close', 'bb_h', 'bb_l']]

#making the MACD indicator
macd = MACD(df['Close']).macd()

#making the rsi indicator
rsi = RSIIndicator(df['Close']).rsi()

#this makes the app
st.write('Stock Bolling Brands')
st.line_chart(bb)

progress_bar = st.progress(0)

st.write("Stock Moving Average Convergence Divergence (MACD)")
st.area_chart(macd)

st.write('Stock RSI')
st.line_chart(rsi)

#put the data in 
st.write('Recent Data')
st.dataframe(df.tail(10))