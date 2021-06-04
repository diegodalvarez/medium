import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import normalize
from sklearn.manifold import TSNE

stocks = pd.read_csv("dataset.csv", index_col = 0)
movements = stocks.values
companies = stocks.index

normalized_movements  = normalize(movements)
model = TSNE(learning_rate = 50)

tsne_feature = model.fit_transform(normalized_movements)

xs = tsne_features[:,0]
ys = tsne_features[:,1]

#then make a scatter plot
fig, ax = plt.subplots(figsize = [15,10])
plt.scatter(xs, ys, alpha = 0.5)

for x, y, company in zip(xs, ys, companies):
    plt.annotate(company, (x,y), fontsize = 9, alpha = 0.75)
    
plt.tight_layout
plt.show()