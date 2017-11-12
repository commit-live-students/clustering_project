# %load q02_hierarchy_clustering/build.py
# Default imports

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from scipy.cluster import hierarchy
from sklearn import datasets
from scipy.cluster.hierarchy import dendrogram, linkage

digits = datasets.load_digits()
X_train=digits.data
y_train=digits.target
df = pd.DataFrame(scale(X_train), index=digits.target)
def hierarchy_clustering(df):
# generate the linkage matrix
    fig = plt.figure()
    ax1 = fig.add_subplot(221)
    Z2 = linkage(df, 'average')
    plt.title('average')
    plt.xlabel('sample index')
    plt.ylabel('distance')
    dendrogram(
        Z2,
        leaf_rotation=90.,  # rotates the x axis labels
        leaf_font_size=8.,  # font size for the x axis labels
    )

    ax2 = fig.add_subplot(222)
    Z3 = linkage(df, 'single')
    plt.title('Single')
    plt.xlabel('sample index')
    plt.ylabel('distance')
    dendrogram(
        Z3,
        leaf_rotation=90.,  # rotates the x axis labels
        leaf_font_size=8.,  # font size for the x axis labels
    )


    ax3 = fig.add_subplot(223)
    Z4 = linkage(df, 'ward')
    plt.title('ward')
    plt.xlabel('sample index')
    plt.ylabel('distance')
    dendrogram(
        Z4,
        leaf_rotation=90.,  # rotates the x axis labels
        leaf_font_size=8.,  # font size for the x axis labels
    )
    ax4 = fig.add_subplot(224)
    Z1 = linkage(df, 'complete')
    plt.title('complete')
    plt.xlabel('sample index')
    plt.ylabel('distance')
    dendrogram(
        Z1,
        leaf_rotation=90.,  # rotates the x axis labels
        leaf_font_size=8.,  # font size for the x axis labels
    )
    plt.show()



# Write your solution here :
