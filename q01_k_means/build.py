# %load q01_k_means/build.py
# Default imports
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from sklearn import datasets


digits = datasets.load_digits()

X_train = digits.images
y_train = digits.target

def k_means(X_train,y_train,cluster=10,random_state=9):
    km = KMeans(init=9, n_clusters=cluster)
    km.fit(X_train.reshape(-1,64))
    km.labels_
    km.cluster_centers_




