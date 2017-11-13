# Default imports
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn import datasets


digits = datasets.load_digits()

X_train = digits.images
y_train = digits.target

# Write your solution here :
def k_means(X_train, y_train, cluster=10, random_state=9):
    km=KMeans(init="random", n_clusters=10).fit(X_train)
    plt.scatter(y_train, X_train[:,0,0], c=km, s=50)
    plt.show()
