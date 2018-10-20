# %load q01_k_means/build.py
# Default imports
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from sklearn import datasets


digits = datasets.load_digits()

X_train = digits.images
y_train = digits.target
import numpy as np
X = np.reshape(X_train, (len(X_train), -1))

def k_means(X_train,y_train,cluster=10,random_state=9):
    km = KMeans(init='random', n_clusters=cluster)
    km.fit(X)
    
    plt.imshow(X)
    plt.show()






