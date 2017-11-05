# Default imports
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn import datasets


digits = datasets.load_digits()

X_train = digits.images
y_train = digits.target

nsamples, nx, ny = X_train.shape
X_train_dataset = X_train.reshape((nsamples,nx*ny))

def k_means(X_train,y_train,cluster = 10,random_state = 9):

    km = KMeans(init="random", n_clusters= cluster )
    km.fit(X_train_dataset)
    l= km.labels_
    cc = km.cluster_centers_
    return

# Write your solution here :
