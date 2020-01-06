# %load q01_k_means/build.py
# Default imports
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from sklearn import datasets


digits = datasets.load_digits()

X_train = digits.data
y_train = digits.target

# Write your solution here :
def k_means(X_train, y_train, cluster = 10, random_state = 9):
    
    k_model = KMeans(init='random',n_clusters=cluster, random_state=random_state)
    k_model.fit(X_train)
    
    for i in range(10):
        plt.figure(figsize=(1,1))
        plt.imshow(k_model.cluster_centers_[i].reshape(8,8))
        plt.show()



k_means(X_train, y_train, cluster = 10, random_state = 9)

