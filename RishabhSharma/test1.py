import numpy as np
import pandas as pd
import seaborn as sns
import xgboost as xgb
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

plt.style.use("seaborn-bright")

#reading the data
data = pd.read_csv("co2.csv")

#cleaining the data so that we can get the month and the year
data['month'] = data.YYYYMM.astype(str).str[4:6].astype(float)
data['year'] = data.YYYYMM.astype(str).str[0:4].astype(float)
data.drop(['YYYYMM'], axis = 1, inplace = True)
data.replace([np.inf, -np.inf], np.nan, inplace = True)

#we are trying to predict value, adn we seperate the data from dates to year and we pass the dates and get the value output
y, X = data.loc[:, 'Value'].values, data.loc[:, ['month', 'year']].values

#making the xgboost model
data_dmatrix = xgb.DMatrix(X, label = y)

#then split the data into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 123)

#now use the XGBRegressor
reg_mod = xgb.XGBRegressor(n_estimators = 1000, learning_rate = 0.08, subsample = 0.75, colsample_bytree = 1, max_depth = 7, gamma = 0)

#fitting the x_train and y_train data
reg_mod.fit(X_train, y_train)

#now get the score
scores = cross_val_score(reg_mod, X_train, y_train, cv = 10)
print("mean cross-validation score:", round(scores.mean(),2))

#now to try to predict the future data
reg_mod.fit(X_train, y_train)
predictions = reg_mod.predict(X_test)

#then use RMSE 
rmse = np.sqrt(mean_squared_error(y_test, predictions))
print("RMSE:", rmse)

#then import the r2 scor
r2 = np.sqrt(r2_score(y_test, predictions))
print("R_squared:", (r2))

#we visualize the original data
plt.figure(figsize = (10, 5), dpi = 80)
sns.lineplot(x = 'year', y = 'Value', data = data)

#then we visualize the original and predicted test data in plot compre how they match up 
plt.figure(figsize = (10,5), dpi = 80)
x_ax = range(len(y_test))

plt.plot(x_ax, y_test, label = 'test')
plt.plot(x_ax, predictions, label ='predicted')
plt.title('Carbon Dioxide Emissions - Test and predicted data')
plt.legend()