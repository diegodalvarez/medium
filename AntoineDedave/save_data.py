import investpy 
import pandas as pd

country = ['united states']
test = investpy.news.economic_calendar(countries = country, from_date = "01/01/2019", to_date = '01/01/2021')
test.to_csv("us_data.csv")

