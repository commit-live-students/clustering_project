# %load q01_k_means/build.py
# Default imports
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn import datasets
import numpy as np

digits = datasets.load_digits()

X_train = digits.images
y_train = digits.target
def k_means(X_train,y_train,cluster=10,random_state=9):
    X=X_train.reshape(1797,64)
#X=np.matrix(zip(X_train,y_train))
    mod=KMeans(n_clusters=cluster,random_state=random_state).fit(X)
#mod.fit(X_train)
#y_pred=mod.predict(y_train)
# Write your solution here :
#y_train.shape
#X_train.shape
    mod.cluster_centers_
