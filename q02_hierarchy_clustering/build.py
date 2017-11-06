import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from scipy.cluster import hierarchy
from sklearn import datasets
from scipy.cluster.hierarchy import dendrogram, linkage
digits = datasets.load_digits()
df = pd.DataFrame(scale(digits.data), index=digits.target)
df
# Write your solution here :
def hierarchy_clustering(X):
    Z = linkage(X, 'average')
    Z[80]
    plt.figure(figsize=(25, 10))

    plt.title('Hierarchical Clustering Dendrogram')
    plt.xlabel('sample index')
    plt.ylabel('distance')
    dendrogram(
        df,
        leaf_rotation=90.,  # rotates the x axis labels
        leaf_font_size=8.,  # font size for the x axis labels
    )
    plt.show()
