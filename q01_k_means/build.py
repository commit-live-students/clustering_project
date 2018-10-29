# %load q01_k_means/build.py
# Default imports
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from sklearn import datasets

digits = datasets.load_digits()

X_train = digits.images
y_train = digits.target
# Write your solution here :
def k_means(X_train,y_train, cluster = 10,random_state = 9):
    X = X_train.reshape((len(X_train), -1))
    kmeans = KMeans(n_clusters= cluster, random_state= random_state).fit(X)
    len_list = []
    limit = 21
    for c in range(0, cluster):
        print('C: ',c)
        image = X_train[(kmeans.labels_ == c) & (y_train == c)]
        temp = len(image)
        for i in range(0, temp):
            if(temp <= limit):
                ax='ax'
                fig = plt.figure()
                value = i+1
                ax += str(value)
                ax = fig.add_subplot(1,temp,i+1)
                plt.axis('off')
                ax.imshow(image[i])
                plt.show()

            else:
                break

