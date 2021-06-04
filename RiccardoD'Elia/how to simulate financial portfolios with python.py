import numpy as np
import pandas_datareader as pdr
import datetime as dt
import pandas_datareader as web
import matplotlib.pyplot as plt
import yfinance as yf

def GBMsimulator(seed, So, mu, sigma, Cov, T, N):

    np.random.seed(seed)
    dim = np.size(So)
    t = np.linspace(0., T, int(N))
    A = np.linalg.cholesky(Cov)
    S = np.zeros([dim, int(N)])
    S[:, 0] = So
    
    for i in range(1, int(N)): 
        
        drift = (mu - 0.5 * sigma**2) * (t[i] - t[i-1])
        Z = np.random.normal(0., 1., dim)
        diffusion = np.matmul(A, Z) * (np.sqrt(t[i] - t[i-1]))
        S[:, i] = S[:, i-1]*np.exp(drift + diffusion)
        
    return S, t

start = dt.datetime(2010,1,1)
end = dt.datetime(2020,1,1)
tickers = ["INTC", 'AMD']

df = yf.download(tickers, start, end)['Adj Close']

seed = 22                       
dim = 2; T = 1; N = int(2.**9)
S0 = np.array([100, 100])

df["intc_log_returns"] = np.log(df['INTC']).diff()
df["amd_log_returns"] = np.log(df['AMD']).diff()

# expected returns
mean_intc = df['intc_log_returns'][1:].mean()
mean_amd = df['amd_log_returns'][1:].mean()
mu = [mean_intc, mean_amd]

# volatility
std_intc = df['intc_log_returns'][1:].std()
std_amd = df['amd_log_returns'][1:].std()
sigma = np.array([std_intc, std_amd])

# covariance matrix
Cov = np.cov(df['intc_log_returns'][1:], df['amd_log_returns'][1:] )


stocks, time = GBMsimulator(seed, S0, mu, sigma, Cov, T, N)

plt.figure(figsize = (16,8))
plt.title('Two-dimensional Correlated Geometric Brownian Motion', fontsize = 18)
plt.plot(time, stocks[0,:], label='Stock 1')
plt.plot(time, stocks[1,:], label='Stock 2')

plt.xlabel('Time', fontsize = 18)
plt.legend(['Stock 1', 'Stock 2'], loc = 'upper left', fontsize = 18)
plt.show()