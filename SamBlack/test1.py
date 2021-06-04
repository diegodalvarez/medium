import decimal
import numpy as np
import pandas as pd
import scipy.linalg
import seaborn as sns
import matplotlib.pyplot as plt

import sklearn
from sklearn import datasets

diabetes = sklearn.datasets.load_diabetes()
df = pd.DataFrame(diabetes.data)
df.columns = diabetes.feature_names
#plot1 = sns.pairplot(df)

cov = np.cov(df.T)

#this is a copy
cov_viz = cov.copy()

np.fill_diagonal(cov_viz, 0)
#plot2 = sns.heatmap(cov_viz, cmap = "coolwarm")

vals, vecs = scipy.linalg.eig(cov)

for i, v in enumerate(vals):
    print("var: {}".format(i+1), decimal.Decimal(v.real))
    
    