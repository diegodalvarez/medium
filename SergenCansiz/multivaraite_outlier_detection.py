import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy.stats import chi2
from matplotlib import patches

#reading the file
df = pd.read_csv("airquality.csv", sep = ',', decimal = '.')

#dropping all of the columns 
df = df[['Ozone', 'Temp']]

#drop values
df = df.dropna()

#then to numpy array
df = df.to_numpy()

plt.scatter(df[:, 0], df[:,1])
plt.title("Scatter Plot")
plt.xlabel("Ozone")
plt.ylabel("Temp")

#now create a covariance matrix
covariance = np.cov(df, rowvar = False)

#covariance matrix to the power of -1
covariance_pm1 = np.linalg.matrix_power(covariance, -1)

#then find the centerpoint
centerpoint = np.mean(df, axis = 0)

#this is going to hold the distances from the centerpoint
distances = []

for i, val in enumerate(df):
    
    p1 = val
    p2 = centerpoint
    
    distance = (p1 - p2).T.dot(covariance_pm1).dot(p1 - p2)
    distances.append(distance)
    
distances = np.array(distances)

#then use the chi-squared distribution
cutoff = chi2.ppf(0.95, df.shape[1])

#then make the outliers 
outlierIndexes = np.where(distances > cutoff)

#print index of outliers
print('---Index of Outlier---')
print(outlierIndexes)

print('Observations found as outlier')
print(df[distances > cutoff, :])

pearson = covariance[0,1] / np.sqrt(covariance[0,0] * covariance[1,1])
ell_radius_x = np.sqrt(1 + pearson)
ell_radius_y = np.sqrt(1 - pearson)

lambda_, v = np.linalg.eig(covariance)
lambda_ = np.sqrt(lambda_)

ellipse = patches.Ellipse(xy = (centerpoint[0], centerpoint[1]), 
                          width = lambda_[0] * np.sqrt(cutoff) * 2,
                          height = lambda_[1] * np.sqrt(cutoff) * 2,
                          angle = np.rad2deg(np.arccos(v[0,0])), 
                          edgecolor = '#fab1a0') 

ellipse.set_facecolor("#0984e3")
ellipse.set_alpha(0.5)

fig = plt.figure()
ax = plt.subplot()
ax.add_artist(ellipse)
plt.scatter(df[:,0], df[:,1])
plt.title("scatter with outlier detection")
plt.xlabel("Ozone")
plt.ylabel("Temp")