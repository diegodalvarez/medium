import shap

from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from sklearn.pipeline import make_pipeline
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split

#load the data
X,y = load_diabetes(return_X_y=True)

#now get features
features = load_diabetes()['feature_names']

#split the data in training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 42)

#make the model
model = make_pipeline(StandardScaler(), MLPRegressor(hidden_layer_size = (5,), activiation = 'logistic', max_iter = 10000,
                                                    learning_rate = 'invscaling', random_state = 0))

#now fit the model
model.fit(X_train, y_train)

#making the explainer object to find the SHAP values
explainer = shap.KernelExplainer(model.predict, X_train)

#calculate the impact on the test dataset
shap_values = explainer.shap_values(X_test, nsamples = 100)
