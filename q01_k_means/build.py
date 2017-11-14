# Default imports
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn import datasets


digits = datasets.load_digits()

X_train = digits.images
y_train = digits.target

# Write your solution here :
import pandas as pd

def k_means(X_train,y_train,cluster = 10,random_state=9):
    cluster = []
    predictions = []
    train = X_train.reshape((X_train.shape[0],X_train.shape[1]*X_train.shape[2]))

    for i in range(10):
        km = KMeans(n_clusters=i,random_state=random_state)
        km.fit(train)
        y_pred = km.predict(train)
        clusters.append(i)
        predictions.append(y_pred)
        plt.plot(clusters,predictions)
        plt.show()
