# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 01:48:44 2020

@author: Diego
"""

#this reads the file
df = pd.read_csv("movie_s_a_dataset.csv", encoding = 'utf-8')

#this trains the data
X_train = df['review'].values
y_train = df['sentiment'].values

#this puts the data into the vector
X_train = vect.transform(X_train)

#this fits the model
clf.fit(X_train, y_train)

pickle.dump(stop, open('stopwords.pkl', 'wb'), protocol = 4)
pickle.dump(clf, open('classifier.pkl', 'wb'), protocol = 4)