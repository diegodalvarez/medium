# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 01:28:53 2020

@author: Diego
"""


# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
# Countries I want to compare
eu_list = ['United Kingdom','France','Germany','Spain','Italy','Sweden']
# Download John Hopkins Data
fp = 'https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_confirmed_global.csv&filename=time_series_covid19_confirmed_global.csv'
df = pd.read_csv(fp).drop(['Province/State','Lat','Long'],axis=1)
# Sum Across Countries/Regions ~ then you get daily differences
df = df.groupby(['Country/Region',]).sum().T.diff()
# Get population of each country
from countryinfo import CountryInfo
pop = {}
for c in eu_list:
    pop[c] = CountryInfo(c).population()
 
pop = pd.DataFrame(pd.DataFrame(pop, index=pop.keys()).ix[0,:])
pop.columns = ['country']
# Adjust all statistics by Population
pop['multiplier'] = 1000000. / pop['country']
df2 = df.copy()
for k in eu_list:
 df2[k] = (df2[k] * pop.ix[k,'multiplier'])
# Plot Infections per million
df[eu_list].cumsum().plot(figsize=(15,7),title = 'Infections per country [Updated up to 20200508]').grid(); plt.show()
# Cases Per Million Population Plot
df2[eu_list].cumsum().plot(figsize=(15,7),title = 'Infections per million, per country [Updated up to 20200508]').grid(); plt.show()
# Cases Per Million Population Plot
df2[eu_list].cumsum().diff(10).plot(figsize=(15,7),title = '10-day change in infections Per Million People [Updated up to 20200508]').grid(); plt.show()