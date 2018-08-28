# %load q01_k_means/build.py
# Default imports
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from sklearn import datasets
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.cluster as cluster
import time
import numpy as np

sns.set_context('poster')
sns.set_color_codes()
plot_kwds = {'alpha' : 0.25, 's' : 80, 'linewidths':0}


digits = datasets.load_digits()

X_train = digits.images
y_train = digits.target

# Write your solution here :
def k_means(X_train,y_train,cluster=10,random_state=9):
    X_train=X_train.reshape(14376,8)
    start_time = time.time()
    km = KMeans( n_clusters=cluster,random_state=random_state)
    km.fit(X_train)
    labels=km.predict(X_train)   
    print(km.cluster_centers_)
    print(km.labels_)
    print(labels)
    palette = sns.color_palette('deep', np.unique(labels).max() + 1)
    colors = [palette[x] if x >= 0 else (0.0, 0.0, 0.0) for x in labels]
    plt.scatter(X_train.T[0], X_train.T[1], c=colors, **plot_kwds)
    frame = plt.gca()
    frame.axes.get_xaxis().set_visible(False)
    frame.axes.get_yaxis().set_visible(False)


