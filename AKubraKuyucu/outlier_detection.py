import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist

data = np.array([[1,2], [2,2], [8,7], [8,9], [7,9], [7,7], [12,10], [25,24], [24,24], [25,25], [25,20], [20,25]])

km = KMeans(n_clusters = 3)
clusters = km.fit_predict(data)

#plt.scatter(*zip(*data), c = clusters, marker = 'x')

#finding the center of the clusters
centroids = km.cluster_centers_

#not sure what this is
points = np.empty((0, len(data[0])), float)

#this will calculat the the distance from the centers to the outliers
distances = np.empty((0, len(data[0])), float)

#getting poitns and distances 
for i, center_elem in enumerate(centroids):
    
    distances = np.append(distances, cdist([center_elem], data[clusters == i], 'euclidean'))
    points = np.append(points, data[clusters == i], axis = 0)
    
#then we make a threshold ratio which just cuts out the percentiles
percentile = 80
outliers = points[np.where(distances > np.percentile(distances, percentile))]

fig = plt.figure()

plt.scatter(*zip(*data), c = clusters, marker = 'x')
plt.scatter(*zip(*outliers), marker = 'o', facecolor = "None", edgecolor = 'r', s = 70)
plt.scatter(*zip(*centroids), marker = 'o', facecolor = 'b', edgecolor = 'b', s = 10)