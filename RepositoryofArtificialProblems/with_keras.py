import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import tensorflow as tf
from keras.layers import Activation, Dense

from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
from sklearn import datasets, decomposition, preprocessing

seed = 42
np.random.seed(seed)
tf.random.set_seed(seed)

n_samples = 1000
n_features = 15

#not sure what this does
x, y, = datasets.make_blobs(
    
    #setting the number of samples
    n_samples = n_samples,
    
    #setting the number of columns, we are sort of making 15 dimensions
    n_features = n_features,
    
    #setting how many clusters we want, this is also going to be the x-axis values
    centers = 2,
    
    #making the range
    center_box = (-4.0, 4.0),
    
    #give the cluster_std
    cluster_std = 1.75,
    
    #setting teh randomness
    random_state = 42
    
    )

#this puts the blobs into with the y and calls them anomaly
df = pd.concat([pd.DataFrame(x), pd.DataFrame({"anomaly":y})], axis = 1)

#make new dataframes that have the 0, and the 1, essentially splitting it by anomaly
normal_events = df[df['anomaly'] == 0]
abnormal_events = df[df['anomaly'] == 1]

#cut out the anomaly column
normal_events = normal_events.loc[:, normal_events.columns != 'anomaly']
abnormal_events = abnormal_events.loc[:, abnormal_events.columns != 'anomaly']

#scale the data, not sure if this is right because source code make some jumps
scaler = StandardScaler()
scaled_data = scaler.fit(normal_events)
scaled_data = scaler.transform(normal_events)


encoder = models.Sequential(name = 'encoder')
encoder.add(layer = layers.Dense(units = 10, activation = activations.relu, input_shape = [n_features]))