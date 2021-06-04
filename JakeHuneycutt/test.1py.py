import numpy as np
import pandas as pd

from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split, cross_val_score


#features
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

#datasets
df = pd.read_csv("https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv", names=names)

#we are trying to find the "class"
X = df.drop('class', axis = 1)

#what we want to predict
y = df['class']

#we wan to split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 66)

#initializing variable
rcf = RandomForestClassifier()

#fit the model
rcf_fit = rcf.fit(X_train, y_train)

#now make the predictions
rcf_predict = rcf_fit.predict(X_test)


#now we want to see the scores
rcf_cv_score = cross_val_score(rcf_fit, X, y, cv = 10, scoring = 'roc_auc')

#print out results
print("=== Confusion Matrix ===")
print(confusion_matrix(y_test, rcf_predict))
print('\n')
print("=== Classification Report ===")
print(classification_report(y_test, rcf_predict))
print('\n')
print("=== All AUC Scores ===")
print(rcf_cv_score)
print('\n')
print("=== Mean AUC Score ===")
print("Mean AUC Score - Random Forest: ", rcf_cv_score.mean())


#tuning with hyperparemeters
##############################################################################

#number of trees in the random forest
n_estimators = [int(x) for x in np.linspace(start = 200, stop = 2000, num = 10)]

#this is number of features at every split
max_features = ['auto', 'sqrt']

#max depth
max_depth = [int(x) for x in np.linspace(100, 500, num = 11)]
max_depth.append(None)

#now create the random grid for hyperparmeters
random_grid = {"n_estimators":"n_estimators", "max_features":"max_features", "max_depth":"max_depth"}

#random search of parameters
rcf_random = RandomizedSearchCV(estimator = rcf, param_distributions = random_grid, n_iter = 100, cv = 3, verbose = 2, random_state = 42, n_jobs = -1)

#fit the model
rcf_random.fit(X_train, y_train)

#print results
print(rcf_random.best_params_)

rcf = RandomForestClassifier(n_estimators=600, max_depth=300, max_features='sqrt')
rcf.fit(X_train,y_train)
rcf_predict = rcf.predict(X_test)
rcf_cv_score = cross_val_score(rcf, X, y, cv=10, scoring='roc_auc')
print("=== Confusion Matrix ===")
print(confusion_matrix(y_test, rcf_predict))
print('\n')
print("=== Classification Report ===")
print(classification_report(y_test, rcf_predict))
print('\n')
print("=== All AUC Scores ===")
print(rcf_cv_score)
print('\n')
print("=== Mean AUC Score ===")
print("Mean AUC Score - Random Forest: ", rcf_cv_score.mean())
