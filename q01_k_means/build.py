# Default imports
from sklearn.cluster import KMeans
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['interactive'] == True

import matplotlib.pyplot as plt


from sklearn import datasets


digits = datasets.load_digits()

X_train = digits.images
y_train = digits.target

# Write your solution here :
def k_means ( X_train, y_train, cluster = 10,random_state = 9):
    model = KMeans(init="k-means++", n_clusters=cluster,random_state=random_state )
    nsamples, nx, ny = X_train.shape
    X_train = X_train.reshape((nsamples,nx*ny))
    labels = model.fit_predict ( X_train )
    plt.scatter(X_train[:, 0], X_train[:, 1], c=labels, s=50, cmap='viridis')
    return

k_means ( X_train, y_train)
#plt.savefig('D:\\output.pdf', format='pdf', dpi=1200)
plt.show()
