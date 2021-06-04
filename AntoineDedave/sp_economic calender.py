import re
import numpy as np
import pandas as pd
import yfinance as yf
import datetime as dt
import plotly.express as px

start = dt.date(2019,1,1)
end = dt.date(2021,1,1)

us_events = pd.read_csv("us_data.csv")

#this deals with fixing the dataframe
def clean_data(dataframe):

    dataframe['date'] = dataframe['date'].fillna(method = 'ffill')
    dataframe = dataframe.drop(dataframe[dataframe['date'].isna()].index)
    dataframe = dataframe.drop(dataframe[dataframe['event'].isna()].index)
    dataframe = dataframe.drop(dataframe[dataframe['actual'].isna()].index) 

    return dataframe

#regex cleaning
def remove_partenthesis(row):
        
    regex = re.compile(".*?\((.*?)\)")
    result = re.findall(regex, row)
    
    ret = row
    for t in result:
        ret = row.replace(t,'')
        
    ret = ret.replace('(','')
    ret = ret.replace(')','')
    ret = ret.replace('[','')
    ret = ret.replace(']','')
    ret = ret.rstrip()
    
    return ret

#something about removing rows
def remove_MoM_QoQ(row):
    
    row = row.replace('MoM','')
    row = row.replace('QoQ','')
    row = row.rstrip()
    
    return row

#converting values of strings to numbers
def convert(el):
    
    #this creates as boolean, is true if el is a string else false
    if isinstance(el, str):
        el = float(el.replace("M", "+e+06").replace("K", "e+03").replace("%", "").replace(",", ".").replace(".00", ""))
        
    elif isinstance(el, int):
        el = float(el)
        
    return el

us_events = clean_data(us_events)
us_events['event'] = us_events['event'].apply(remove_partenthesis).apply(remove_MoM_QoQ)

#then create a pivot table
pivot_table = us_events.pivot_table(values = "actual", index = ['date'], columns = ['event'], aggfunc = lambda x: x)
pivot_table.index = pd.to_datetime(pivot_table.index)

sp = yf.download("^GSPC", start, end)
calendar = sp.merge(pivot_table, how = 'outer', left_on = sp.index, right_index = True)
#calendar = calendar.select_dtypes(include = ['float64']).fillna(method = 'ffill')

#correlation matrix
corr = calendar.corr()
corr = np.abs(corr)

fig = px.imshow(corr)
fig.show()