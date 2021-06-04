import seaborn as sns
import numpy as np

df = sns.load_dataset("iris")

mean, cov = [0,1], [(1, 0.5), (0.5, 1)]
data = np.random.multivariate_normal(mean, cov, 200)