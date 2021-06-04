# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 01:46:59 2020

@author: Diego
"""

#this turns all of the words into vectors 
vect = HashingVectorizer(decode_error = 'ignore', n_features = 2**21, preprocessor = None, tokenizer = tokenizer)

#this is the classifier
clf = SGDClassifier(loss = 'log', random_state = 1, max_iter = 100, early_stopping = False)