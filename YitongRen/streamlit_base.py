import pandas as pd
import yfinance as yf
import datetime as dt
import streamlit as st
import pandas_datareader as web
import matplotlib.pyplot as plt

st.Title("covariance GBM")

def get_recommendations(input_ticker):

    tickerSymbol = input_ticker
    tickerData = yf.Ticker(tickerSymbol)
    
    recommendations = tickerData.recommendations
    
    today = dt.date.today()
    year = today.year
    first_date = dt.datetime(year, 1, 1)
    
    
    for dates in recommendations.index:
        
        if dates < first_date:
            recommendations = recommendations.drop(dates)
            
    return recommendations

today = dt.date.today()

#not sure what this is
before = today - dt.timedelta(days = 700)

start_date = st.sidebar.date_input("Start Date", before)
end_date = st.sidebar.date_input("End Date", today)

if start_date < end_date:
    st.sidebar.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
    
else:
    st.sidebar.error("Error: end date must fall after the start date")

first_graph, second_graph = False, False

#stock 1 
st.header("First Stock")
first_ticker = st.text_input("Input first ticker here")
first_status_radio  = st.radio("select search when first stock is ready", ('Entry', 'Search'))

if first_status_radio == "Search":
    
    st.header("Stock recommendations for this calender year")
    first_recommendation = get_recommendations(first_ticker)
    st.dataframe(first_recommendation)
    
    st.header("historical stock prices")
    first_df = web.DataReader(first_ticker, 'yahoo', start_date, end_date)
    st.dataframe(first_df)
    
    first_graph = True

#stock 2 
st.header("Second Stock")
second_ticker = st.text_input("Input second ticker here")
second_status_radio  = st.radio("select search when second stock is ready", ('Entry', 'Search'))

if second_status_radio == "Search":
    
    st.header("Stock recommendations for this calender year")
    second_recommendation = get_recommendations(second_ticker)
    st.dataframe(second_recommendation)
    
    st.header("historical stock prices")
    second_df = web.DataReader(second_ticker, 'yahoo', start_date, end_date)
    st.dataframe(second_df)
    
    second_graph = True


tickers = [first_ticker, second_ticker]

if first_graph == True and second_graph == True:
    
    df_adj = web.DataReader(tickers, 'yahoo', start_date, end_date)['Adj Close']
    
    fig1 = plt.scatter(df_adj.index, df_adj.columns, '-o')
    st.pyplot(fig1)
    
    print(df_adj)
