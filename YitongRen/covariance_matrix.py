import numpy as np
import matplotlib.pyplot as plt

#setting two different expected returns
mu_a, mu_b = 0.2, 0.3

#setting two different expected volatility
sig_a, sig_b = 0.25, 0.35
 
#we want the starting price for the stock
s0_a, s0_b = 60, 55 

#we need to make a total amount of time and discretize the times 
T = 1
delta_t = 0.001

#this will be the number of steps in the function
steps = T / delta_t

#now we make a correlation variable
rho = 0.2

#now we make a correlation matrix
cor_matrix = np.array([[1.0, rho], [rho, 1.0]])

#now we want to get the diagnal matix
sd = np.diag([sig_a, sig_b])

#now we want to get the standard normal and multiply it by the covariance matrix
cov_matrix = np.dot(sd, np.dot(cor_matrix, sd))

#then use the cholesky decomposition
L = np.linalg.cholesky(cov_matrix)

plt.figure(figsize = (12,6))

#start with the beginning of the paths
path_a = [s0_a]
path_b = [s0_b]

'''
then we make these new variables probably because the for loop is going to 
change them and we need to put in initial values
'''
st_a, st_b = s0_a, s0_b

#go over all the steps
for i in range(int(steps)):
    
    #not sure what this is
    V = L.dot(np.random.normal(0,1,2))
    
    #this looks like it is doing something with changing the standard deviation
    
    st_a = st_a * np.exp((mu_a - 0.5 * sig_a ** 2) * delta_t + sig_a * np.sqrt(delta_t) * V[0])
    st_b = st_b * np.exp((mu_b - 0.5 * sig_b ** 2) * delta_t + sig_b * np.sqrt(delta_t) * V[1])
    
    #then append that into the path
    path_a.append(st_a)
    path_b.append(st_b)
    
#now we want to plot it
plt.plot(path_a, label = "stock A", linewidth = 2)
plt.plot(path_b, label = "stock B", linewidth = 2)

plt.legend()
plt.title('Correlated Stock movement Using monte carlo simulation')
plt.ylabel("stock price")
plt.xlabel('steps')
