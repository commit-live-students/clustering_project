# Default imports
from sklearn.cluster import KMeans
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.preprocessing import scale
from sklearn.decomposition import PCA


digits = datasets.load_digits()

X_train = digits.data
y_train = digits.target

# Write your solution here :
def k_means(X_train,y_train,cluster=10,random_state=9):
    model = KMeans(n_clusters=cluster,random_state=random_state)
    pca = PCA(n_components=2)
    reduced_X = pca.fit_transform(X_train)
    model.fit(reduced_X)
    ans = model.predict(reduced_X)
    plt.plot(reduced_X)
    plt.plot(ans)
    plt.show()
