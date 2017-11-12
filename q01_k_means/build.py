# %load q01_k_means/build.py
# Default imports
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn import datasets


digits = datasets.load_digits()

X_train = digits.images
y_train = digits.target

def k_means(X_train,y_train,cluster=10,random_state=9):
    pass
