from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn import datasets


digits = datasets.load_digits()

X_train = digits.images
y_train = digits.target


def k_means(X_train, y_train, cluster=10, random_state=9):
    X = X_train.reshape((len(X_train), -1))
    kmeans = KMeans(n_clusters=cluster, random_state=random_state).fit(X, y_train)
    a = X_train[(y_train == 0) & (kmeans.labels_ == 0)][0:20]
    b = X_train[(y_train == 1) & (kmeans.labels_ == 1)][0:20]
    c = X_train[(y_train == 2) & (kmeans.labels_ == 2)][0:20]
    d = X_train[(y_train == 3) & (kmeans.labels_ == 3)][0:20]
    e = X_train[(y_train == 4) & (kmeans.labels_ == 4)][0:20]
    f = X_train[(y_train == 5) & (kmeans.labels_ == 5)][0:20]
    g = X_train[(y_train == 6) & (kmeans.labels_ == 6)][0:20]
    h = X_train[(y_train == 7) & (kmeans.labels_ == 7)][0:20]
    i = X_train[(y_train == 8) & (kmeans.labels_ == 8)][0:20]
    j = X_train[(y_train == 9) & (kmeans.labels_ == 9)][0:20]
    for char in (a, b, c, d, e, f, g, h, i, j):
        for index in range(0, len(char)):
            plt.subplot(10, 20, index + 1)
            plt.axis('off')
            plt.imshow(char[index])
        plt.show()


