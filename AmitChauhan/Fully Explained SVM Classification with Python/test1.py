import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

#reading data
dataset = pd.read_csv("Social_Network_Ads.csv")

#then we are cutting the values it seems like what they are doing is that the dataset has gender, age, esimatedSalary, and purchased
#we are trying to predict purchase

#this will gives us all the rows in Age, Esimtaed salary
X = dataset.iloc[:, [2,3]].values

#this will give us the output
y = dataset.iloc[:, 4].values

#divide the data into training and testing data, and we are using 75% of the data to predict 25%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

#we also wanto scale

#make the scaler object
sc = StandardScaler()

#then use it to scale the data
X_train = sc.fit_transform(X_train)

#unsure on why this one if transform and not fit_transform
X_test = sc.transform(X_test)

#here is where we decide the classifier
classifier = SVC(kernel = "linear", random_state = 0)

#then we want to fit the data
classifier.fit(X_train, y_train)

#not sure what this is
#SVC(C = 1.0, cache_size = 200, class_weight = None, coef0 = 0.0, decision_function_shape = "ovr", degree = 3, gamma = "auto_deprecated", kernel = "linaer", max_iter = -1, probability = False, random_state = 0, shrinking = True, tol = 0.001, verbose = False)

#make the predictions
y_pred = classifier.predict(X_test)

#not sure what this does
cm = confusion_matrix(y_test, y_pred)

#this will deal with plotting
X_set, y_set = X_train, y_train

X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01), np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))

plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape), alpha = 0.5, cmap = ListedColormap(('red', 'green')))

plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())

for i, j in enumerate(np.unique(y_set)):
    
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1], alpha = 0.5, c = ListedColormap(('red', 'green'))(i), label = j)
    
plt.title('SVM (Training Set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()

X_set, y_set = X_test, y_test

X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:,0].max() + 1, step = 0.01), np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape), alpha = 0.5, cmap = ListedColormap(('red', 'green')))

plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())

for i, j in enumerate(np.unique(y_set)):
    
   plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1], alpha=0.9, c = ListedColormap(('red', 'green'))(i), label = j)
   
plt.title("SVM (Test set)")
plt.xlabel("Age")
plt.ylabel("Estimated Salary")
plt.legend()
plt.show()
   
   
