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




X_train = df
y_train = df.index
# Write your solution here :
def hierarchy_clustering(X_train):
    # generate the linkage matrix
    Z = linkage(X_train, 'ward')
    # calculate full dendrogram
    plt.figure(figsize=(25, 10))
    plt.title('Hierarchical Clustering Dendrogram')
    plt.xlabel('sample index')
    plt.ylabel('distance')
    dendrogram(
        Z,
        leaf_rotation=90.,  # rotates the x axis labels
        leaf_font_size=8.,  # font size for the x axis labels
    )

    plt.show()


