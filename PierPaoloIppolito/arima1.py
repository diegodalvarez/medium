import warnings
import numpy as np
import pandas as pd
import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt

from pandas.plotting import lag_plot
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error

warnings.filterwarnings('ignore', 'statsmodels.tsa.arima_model.ARMA',
                        FutureWarning)
warnings.filterwarnings('ignore', 'statsmodels.tsa.arima_model.ARIMA',
                        FutureWarning)

#.warn(ARIMA_DEPRECATION_WARN, FutureWarning)

#read data
df = pd.read_csv("msft.csv").fillna(0)

#looking at autocorrelation feature
def plot_autcorrelation(df_input, lag_time):
    
    #get first and ending dates for plotting
    start_date = df_input['Date'][0]
    end_date = df_input['Date'][len(df_input) - 1]
    
    #plot the lag corerlation
    plt.figure(figsize=(10,10))
    lag_plot(df_input['Open'], lag = lag_time)
    plt.title("Microsoft {}".format(lag_time) + " days Autocorrelation plot for {}".format(start_date) + " to {}".format(end_date))
    
#five_day_lag = plot_autcorrelation(df, 5)

#plotting our cutoff spot for train test 
def plot_train_test_plot(df_input, cutoff):
    
    #this gets the cutoff size
    train_data, test_data = df_input[0: int(len(df_input) * cutoff)], df_input[int(len(df_input) * cutoff):]
    
    #then do the plotting
    plt.figure(figsize=(12,7))
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title("Microsoft Open Price")
    plt.plot(df_input['Open'], 'blue', label = 'Training Data')
    plt.plot(test_data['Open'], 'green', label = 'Testing Data')
    plt.xticks(np.arange(0, len(df_input) + 1, 1300), df_input['Date'][0: len(df_input) + 1: 1300])
    plt.legend()

    return train_data, test_data

train_data, test_data = plot_train_test_plot(df, 0.8)


def sample_kun(y_true, y_pred):
    return np.mean((np.abs(y_pred - y_true) * 200 / (np.abs(y_pred) + np.abs(y_true))))

def make_arima(test, train, p, d, q):
    
    #load the data
    train_ar = train['Open'].values
    test_ar = test['Open'].values
    
    #this is making a slot for all of the train data
    history = [x for x in train_ar]
    print(type(history))
    
    #then it makes space for our predictions
    predictions = list()
    
    #then we are going to make the model
    
    #first loop through all of the values of test_ar
    for t in range(len(test_ar)):
        
        #make the model
        model = ARIMA(history, order = (p,d,q))
        
        #this the model
        model_fit = model.fit(disp=0)
        
        #then put the ouptu in our list
        output = model_fit.forecast()
        
        #not sure what this is, think it has something to do with what we observed
        yhat = output[0]
        
        #then put the prediction 
        predictions.append(yhat)
        
        #not sure what this is, looks like something that you add in for our observation
        obs = test_ar[t]
        
        #put those observations into the history list
        history.append(obs)
        
    #use our first error method
    error = mean_squared_error(test_ar, predictions)
    
    #then print out that 
    print("Testing Mean Squared Error: %.3f" % error)
    
    #second error method and print
    error2 = sample_kun(test_ar, predictions)
    print("Symmetric Mean abslolute percentage error: %.3f" % error2)
        
test_run = make_arima(train_data, test_data, 5, 1, 0)

