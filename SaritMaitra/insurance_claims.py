import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("insurance_claims.csv")

table = pd.crosstab(df.age, df.fraud_reported)
table.div(table.sum(1).astype(float), axis = 0).plot(kind = 'bar', stacked = True)