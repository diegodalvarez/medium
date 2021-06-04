import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.metrics import roc_auc_score

from pyod.models.copod import COPOD
from pyod.utils.data import generate_data
from pyod.utils.data import evaluate_print
from pyod.utils.example import visualize
from pyod.utils.utility import precision_n_scores

#generating random data
X_train, y_train, X_test, y_test = generate_data(n_train = 200, n_test = 100, n_features = 5, contamination = 0.1, random_state = 3)

#not sure what this is doing looks like standardizing 
X_train = X_train * np.random.uniform(0, 1, size = X_train.shape)
X_test = X_test * np.random.uniform(0, 1, size = X_test.shape)

clf_name = 'COPOD'
clf = COPOD()
clf.fit(X_train)
test_scores = clf.decision_function(X_test)

#gets us some score
roc = round(roc_auc_score(y_test, test_scores), ndigits = 4)

#gets some other score
prn = round(precision_n_scores(y_test, test_scores), ndigits = 4)

print(f'{clf_name} Roc:{roc}, precision @ rank n:{prn}')

#concaenating data
X = np.concatenate([X_train, X_test], axis = 0)
ys = np.concatenate([y_train, y_test])

#outlier
detector = COPOD()
scores = detector.decision_function(X)

#plotting
sns.distplot(scores[ys==0], label = "inlier scores")
sns.distplot(scores[ys==1], label = "outlier scores").set_title("Distribution of Outlier scores from unfitted COPOD detector")
plt.legend()
plt.xlabel("Outlier score")

#anomaly explanation
train_outliers_idx = np.where(y_train==1)[0]
for idx in train_outliers_idx:
    clf.explain_outlier(idx, cutoffs = None, feature_names = None)