import numpy as np

from pyod.models.copod import COPOD
from pyod.utils.example import visualize
from pyod.utils.data import generate_data, evaluate_print

#not sure what this is
contamination = 0.1

#200 training data set
n_train = 200

#100 test training
n_test = 100

#making the data
X_train, y_train, X_test, y_test = generate_data(n_train = n_train, n_test = n_test, n_features = 2, contamination = contamination, random_state = 42)

#name of the model
clf_name = "COPOD"

#making the classifier
clf = COPOD()

#traing the data
clf.fit(X_train)

#get the prediction
y_train_pred = clf.labels_

#this get the outlier scores
y_train_scores = clf.decision_scores_

#get the prediction on the test data
y_test_pred = clf.predict(X_test)

#get the outlier scores
y_test_scores = clf.decision_function(X_test)

#print the data
print("\nOn Training Data:")
evaluate_print(clf_name, y_train, y_train_scores)
print("\nOn Test Data:")
evaluate_print(clf_name, y_test, y_test_scores)

visualize(clf_name, X_train, y_train, X_test, y_test, y_train_pred, y_test_pred, show_figure = True, save_figure = False)