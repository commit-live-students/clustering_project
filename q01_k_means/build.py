# Default imports
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn import datasets


digits = datasets.load_digits()

X_train = digits.images
y_train = digits.target

# Write your solution here :
def k_means (X_train,y_train,cluster=10,random_state=9):
    x=[]
    y=[]
    nsamples, nx, ny = X_train.shape
    d2_train_dataset = X_train.reshape((nsamples,nx*ny))
    for i in range(1,cluster):
        km = KMeans(n_clusters=i,random_state=random_state)
        km.fit(d2_train_dataset)
        y_pred = km.predict(d2_train_dataset)
        x.append(i)
        y.append(y_pred)
        plt.plot(x,y)
        plt.show()
     
