import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets, decomposition, preprocessing

#not sure what this does
x, y, = datasets.make_blobs(
    
    #setting the number of samples
    n_samples = 500,
    
    #setting the number of columns, we are sort of making 15 dimensions
    n_features = 15,
    
    #setting how many clusters we want, this is also going to be the x-axis values
    centers = 2,
    
    #making the range
    center_box = (-4.0, 4.0),
    
    #give the cluster_std
    cluster_std = 1.75,
    
    #setting teh randomness
    random_state = 42
    
    )

#now we are making the data be between [0,1]
x = preprocessing.MinMaxScaler().fit_transform(x)

#i think this means make the there will be three dimensions, but not sure
pca = decomposition.PCA(n_components = 3)

#this is making the PCA
pca_result = pca.fit_transform(x)

#printing the variance
print(pca.explained_variance_ratio_)

#then we are just putting this into a dataframe, and it seems like we don't put in y
pca_df = pd.DataFrame(data = pca_result, columns = [ 'pc_1', 'pc_2', 'pc_3'])

#now we add in the y values and call them label
pca_df = pd.concat([pca_df, pd.DataFrame({'label': y})], axis = 1)

#now we want to make a 3d graph
ax = Axes3D(plt.figure(figsize = (8,8)))

#then we make the scatter plot
ax.scatter(xs = pca_df['pc_1'], ys = pca_df['pc_2'], zs = pca_df['pc_3'], c = pca_df['label'], s = 25)

#then name the axis
ax.set_xlabel("pc_1")
ax.set_ylabel("pc_2")
ax.set_zlabel("pc_3")
plt.show()