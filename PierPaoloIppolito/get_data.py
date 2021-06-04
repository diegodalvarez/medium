import pandas as pd
import yfinance as yf
import datetime as dt

end = dt.datetime.today()
start = end - dt.timedelta(days = (40*365))
msft = yf.download("MSFT", start, end)
msft.to_csv("msft.csv")