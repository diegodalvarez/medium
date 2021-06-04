import time
import requests
import selenium 
import numpy as np
import pandas as pd
import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt


#company ticker
company_ticker = "SM"

#this is optional but it is the company name
company_name = "SM Energy"

#they find the probablity of default by finding the market-implied default probability
#normally they take a 1 year approach
#they compare the market-implied default probabiliteis with the S&P one-year transition rates for global credit 
#the transition matrix shows the observed historical probabilities ofa particular rating transitioing to another rating

#use selenium script to get the FINRA's TRACE bond data 
#they are using selenium with a chromedriver

ticker = yf.Ticker("AAPL")
name = ticker.info