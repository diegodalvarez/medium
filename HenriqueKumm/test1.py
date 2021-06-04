import numpy as np
import pandas as pd
import yfinance as yf
import datetime as dt
import matplotlib.pyplot as plt

from sklearn import linear_model
from sklearn.model_selection import KFold
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler

tickers = ["JPM", "BAC", "C"]
end = dt.datetime.today()
start = end - dt.timedelta(days = (10 * 365) + 3)

df = yf.download(tickers, start, end)['Adj Close']

for i in df.columns:
    
    df[i+"_ret"] = df[i].pct_change()
    df[i+"_momentum"] = df[i] - df[i].shift(-1)
    df[i+"_sma"] = df[i].rolling(window = 10).mean()
    df[i+"_ema"] = df[i].ewm(span = 10).mean()
    
df = df.dropna().reindex(sorted(df.columns), axis = 1)

cols = df.columns.tolist()
cols.remove("BAC")
cols.remove("C")
cols.remove("JPM")

bac_col = cols[0:4]
c_col = cols[5:8]
jpm_col = cols[9:12]

bac_ml = df[bac_col]

gnb = GaussianNB()
scaler = StandardScaler()
scaler.fit(bac_ml)

bac_ml_scaled = pd.DataFrame(scaler.transform(bac_ml))
bac_ml_scaled.columns = bac_ml.columns

y = bac_ml['BAC_ret'].values
X = bac_ml_scaled[bac_ml_scaled.columns].shift(-1).fillna(0).values
kf = KFold(n_splits = 5, shuffle = True)
kf.get_n_splits(X)

for train_index, test_index in kf.split(X):
    
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    
gnb.fit(pd.DataFrame(X_train), np.sign(y_train))

'''
dfyGNB = pd.DataFrame(y_test)
dfyGNB.columns = ["Returns"]
dfyGNB['NB_pred'] = gnb.predict(pd.DataFrame(X_test))
dfyGNB['log_p1'] = pd.DataFrame(gnb.predict_proba(pd.DataFrame(X_test)))[0]
dfyGNB['log_p2'] = pd.DataFrame(gnb.predict_proba(pd.DataFrame(X_test)))[1]
dfyGNB['log_p3'] = pd.DataFrame(gnb.predict_proba(pd.DataFrame(X_test)))[2]
dfyGNB['p'] = dfyGNB[['log_p1', 'log_p2', 'log_p3']].max(axis=1)

dfyGNB['NB_returns'] = dfyGNB['Returns'] * dfyGNB['NB_pred']
dfyGNB["Kelly_NB_returns"] = dfyGNB['Returns'] * dfyGNB['NB_pred'] * (((2*(dfyGNB['p']))-1)/2)
dfyGNB[['Returns', 'NB_returns', 'Kelly_NB_returns']].cumsum().apply(np.exp).plot(figsize=(10, 6))
'''

lm = linear_model.LogisticRegression(C = 1e5, dual=True, solver = 'liblinear', max_iter = 1000, multi_class = 'ovr')

lm.fit(pd.DataFrame(X_train), np.sign(y_train))
dfy = pd.DataFrame(y_test)
dfy.columns = ["Returns"]


dfy['SMA'] = bac_ml_scaled['BAC_sma']
dfy['log_pred'] = lm.predict(pd.DataFrame(X_test))
dfy['log_p1'] = pd.DataFrame(lm.predict_proba(pd.DataFrame(X_test)))[0]
dfy['log_p2'] = pd.DataFrame(lm.predict_proba(pd.DataFrame(X_test)))[1]
dfy['log_p3'] = pd.DataFrame(lm.predict_proba(pd.DataFrame(X_test)))[2]
dfy['p'] = dfy[['log_p1', 'log_p2', 'log_p3']].max(axis=1)
dfy['log_returns'] = dfy['Returns'] * dfy['log_pred']
dfy["Kelly_log_returns"] = dfy['Returns'] * dfy ['log_pred'] * (((2*(dfy['p']))-1)/2)
dfy[['Returns', 'log_returns', 'Kelly_log_returns']].cumsum().apply(np.exp).plot(figsize=(10, 6))
sum(1 for x in dfy['log_returns'] if x > 0)/len(dfy['log_returns'])