# %load q01_k_means/build.py
# Default imports
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn import datasets


digits = datasets.load_digits()

X_train = digits.images
y_train = digits.target
import numpy as np
X = np.reshape(X_train, (len(X_train), -1))
# Write your solution here :

def k_means(X_train,y_train,cluster=10,random_state=9):
    km = KMeans(init='random', n_clusters=cluster)
    km.fit(X)
    
    plt.imshow(X)
    plt.show()
    




def k_means(X_train,y_train,cluster=10,random_state=9):
    km = KMeans(init='random', n_clusters=cluster)
    km.fit(X)
    
    plt.imshow(km.cluster_centers_)
    plt.show()
    
km = KMeans(init='random', n_clusters=10)

import pandas as pd
X_train.shape
len(X_train)
import numpy as np
X = np.reshape(X_train, (len(X_train), -1))
km.fit(X)
km.labels_.shape
plt.figure(figsize=(10,5))
plt.imshow(km.labels_.reshape(-1,1))
plt.show()
km.cluster_centers_.shape



