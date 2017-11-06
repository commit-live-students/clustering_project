# %load q01_k_means/build.py
# Default imports
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn import datasets
import pandas as pd
import numpy as np
import time
import seaborn as sns

digits = datasets.load_digits()

X_train = digits.images
y_train = digits.target
print(X_train.shape)
print(y_train.shape)
# Write your solution here :


def k_means(X_train,y_train,cluster=10,random_state=9):
    X = np.reshape(X_train, (len(X_train), -1))
    data=X
    for i in range(cluster):
        #print(i)

        km = KMeans(init="random", n_clusters=i+1)
        #y=km.fit_predict(X)
        #print(y)
        labels =km.fit_predict(data)
        #end_time = time.time()
        palette = sns.color_palette('deep', np.unique(labels).max() + 1)
        colors = [palette[x] if x >= 0 else (0.0, 0.0, 0.0) for x in labels]
        plt.scatter(data.T[0], data.T[1])
        frame = plt.gca()
        frame.axes.get_xaxis().set_visible(False)
        frame.axes.get_yaxis().set_visible(False)
        #plt.title('Clusters found by {}'.format(str(algorithm.__name__)), fontsize=24)
        #plt.text(5, 10, 'Clustering took {:.2f} s'.format(end_time - start_time), fontsize=14)
        plt.show()



#k_means(X_train,y_train,cluster=10,random_state=9)
