# %load q01_k_means/build.py
# Default imports
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from sklearn import datasets

digits = datasets.load_digits()
X_train = digits.images
y_train = digits.target

def k_means(X_train, y_train, cluster=10, random_states=9):
    kmeans = KMeans(n_clusters=cluster, random_state=random_states)
    clusters = kmeans.fit_predict(digits.data)
    centers = kmeans.cluster_centers_.reshape(10, 8, 8)
    fig, ax = plt.subplots(1, 10, figsize=(8, 3))
    centers = kmeans.cluster_centers_.reshape(10, 8, 8)
    for axi, center in zip(ax.flat, centers):
        axi.set(xticks=[], yticks=[])
        axi.imshow(center, interpolation='nearest', cmap='viridis')
    plt.show();



