#this looks like it makes the alert

import pandas as pd 

symbols = pd.read_csv("watchlist.csv")
symbols = list(symbols.Symbols.values)

