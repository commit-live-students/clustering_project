# Default imports

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from scipy.cluster import hierarchy
from sklearn import datasets

digits = datasets.load_digits()
df = pd.DataFrame(scale(digits.data), index=digits.target)

# Write your solution here :
# Write your solution here f
def hierarchy_clustering(X):
    Z=linkage(X,'average')
    Z[80]
    plt.figure(figsize=(25,10))
    plt.title('Hierarchial Clustering')
    plt.xlabel('sample index')
    plt.ylabel('distance')
    dendrogram(
    df,
    leaf_rotation=90.,
    leaf_font_size=8.,
    )
    return plt.show()
