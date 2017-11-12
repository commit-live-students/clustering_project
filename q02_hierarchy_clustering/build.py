# %load q02_hierarchy_clustering/build.py
# Default imports

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from scipy.cluster import hierarchy
from sklearn import datasets
from scipy.cluster.hierarchy import dendrogram, linkage

digits = datasets.load_digits()
df = pd.DataFrame(scale(digits.data), index=digits.target)

#print(df.head)
# Write your solution here :

def hierarchy_clustering(df):
    Z_single = linkage(df, 'single')
    Z_avg = linkage(df, 'average')
    z_ward=linkage(df, 'ward')
    z_comp=linkage(df,'complete')
    plt.figure(figsize=(25, 10))
    plt.title('Hierarchical Clustering Dendrogram')
    plt.xlabel('sample index')
    plt.ylabel('distance')
    plt.subplot(1,2,1)

    dendrogram(
        Z_single,
        leaf_rotation=90.,  # rotates the x axis labels
        leaf_font_size=8.,  # font size for the x axis labels
    )
    plt.subplot(2,2,1)
    dendrogram(
        z_comp,
        leaf_rotation=90.,  # rotates the x axis labels
        leaf_font_size=8.,  # font size for the x axis labels
    )
    plt.subplot(2,2,2)
    dendrogram(
        Z_avg,
        leaf_rotation=90.,  # rotates the x axis labels
        leaf_font_size=8.,  # font size for the x axis labels
    )
    plt.subplot(1,2,2)
    dendrogram(
        z_ward,
        leaf_rotation=90.,  # rotates the x axis labels
        leaf_font_size=8.,  # font size for the x axis labels
    )
    plt.show()

#hierarchy_clustering(df)
