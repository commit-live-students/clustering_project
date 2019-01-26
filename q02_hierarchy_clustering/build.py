# %load q02_hierarchy_clustering/build.py
# Default imports

import pandas as pd
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from sklearn.preprocessing import scale
from scipy.cluster import hierarchy
from sklearn import datasets
from scipy.cluster.hierarchy import dendrogram, linkage
digits = datasets.load_digits()
df = pd.DataFrame(scale(digits.data), index=digits.target)
X_train=df.iloc[:, :-1]
y_train=df.iloc[:, :-1]
def hierarchy_clustering(df):
    Z = linkage(df, 'average')
    Z1 = linkage(df, 'complete')
    Z2 = linkage(df, 'single')
    Z3= linkage(df, 'ward')
    plt.figure(figsize=(25, 10))
    plt.subplot(1,1,4)
    plt.title('Hierarc	hical Clustering Dendrogram')
    plt.xlabel('sample index')
    plt.ylabel('distance')
    dendrogram(Z,leaf_rotation=90,leaf_font_size=8.,) 
    plt.subplot(1,2,4)
    plt.title('Hierarc	hical Clustering Dendrogram')
    plt.xlabel('sample index')
    plt.ylabel('distance')
    dendrogram(Z1,leaf_rotation=90,leaf_font_size=8.,)
    plt.subplot(2,1,4)
    plt.title('Hierarc	hical Clustering Dendrogram')
    plt.xlabel('sample index')
    plt.ylabel('distance')
    dendrogram(Z2,leaf_rotation=90,leaf_font_size=8.,) 
    plt.subplot(2,2,4)
    plt.title('Hierarc	hical Clustering Dendrogram')
    plt.xlabel('sample index')
    plt.ylabel('distance')
    dendrogram(Z3,leaf_rotation=90,leaf_font_size=8.,) 
    plt.show()



