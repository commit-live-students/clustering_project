# Default imports
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn import datasets


digits = datasets.load_digits()

X_train = digits.images
y_train = digits.target

def k_means(X_train,y_train,cluster=10,random_state1=9):

    km = KMeans(n_clusters=cluster , random_state = random_state1)
    km.fit(X_train,y_train)
    km.labels_

    plt.show()
