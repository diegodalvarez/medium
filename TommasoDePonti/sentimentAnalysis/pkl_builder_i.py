import re
import nltk
import pickle
import pandas as pd

nltk.download('stopwords')

from nltk.corpus import stopwords
from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import HashingVectorizer

