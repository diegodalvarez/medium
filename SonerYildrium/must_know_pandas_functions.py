import numpy as np
import pandas as pd

#generate synthetic data
df = pd.DataFrame({
    "date": pd.date_range(start = "2020-05-01", periods = 100, freq = 'D'),
    "temperature": np.random.randint(18, 30, size = 100) + np.random.random(100).round(1)
    })

#shift function
df["temperature_lag_1"] = df['temperature'].shift(1)

#use fill function to get rid of NaNs
df['temperature_lag_1'] = df['temperature'].shift(1, fill_value = df.temperature.mean())

#we can use the resample function to get it via group, i'm pretty sure this gets the mean of the week
df_weekly = df.resample("W", on = 'date').mean()

#using the asfreq function to resample to get the end of a period value
df_asfreq = df.set_index("date").asfreq('W').head()