# %load q02_hierarchy_clustering/build.py
# Default imports

import pandas as pd
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from sklearn.preprocessing import scale
from scipy.cluster import hierarchy
from sklearn import datasets

digits = datasets.load_digits()
#df = pd.DataFrame(scale(digits.data), index=digits.target)
# Write your solution here :
def hierarchy_clustering(X_train):
    
    df = pd.DataFrame(scale(X_train))
    plt.subplot(1,4,1)
    Z = hierarchy.linkage(df,'complete')
    hierarchy.dendrogram(Z,leaf_rotation=90,leaf_font_size=8)
    plt.title('Complete linkage')
    plt.plot()

    plt.subplot(1,4,2)
    Z = hierarchy.linkage(df,'average')
    hierarchy.dendrogram(Z,leaf_rotation=90,leaf_font_size=8)
    plt.title('Average linkage')
    plt.plot()

    plt.subplot(1,4,3)
    Z = hierarchy.linkage(df,'single')
    hierarchy.dendrogram(Z,leaf_rotation=90,leaf_font_size=8)
    plt.title('Single linkage')
    plt.plot()

    plt.subplot(1,4,4)
    Z = hierarchy.linkage(df,'ward')
    hierarchy.dendrogram(Z,leaf_rotation=90,leaf_font_size=8)
    plt.title('Ward')
    plt.plot()

    plt.show()

hierarchy_clustering(digits.data)
# plt.subplot(1,4,1)
# Z = hierarchy.linkage(df,'complete')
# hierarchy.dendrogram(Z,leaf_rotation=90,leaf_font_size=8)
# plt.title('Complete linkage')
# plt.plot()

# plt.subplot(1,4,2)
# Z = hierarchy.linkage(df,'average')
# hierarchy.dendrogram(Z,leaf_rotation=90,leaf_font_size=8)
# plt.title('Average linkage')
# plt.plot()

# plt.subplot(1,4,3)
# Z = hierarchy.linkage(df,'single')
# hierarchy.dendrogram(Z,leaf_rotation=90,leaf_font_size=8)
# plt.title('Single linkage')
# plt.plot()

# plt.subplot(1,4,4)
# Z = hierarchy.linkage(df,'ward')
# hierarchy.dendrogram(Z,leaf_rotation=90,leaf_font_size=8)
# plt.title('Ward')
# plt.plot()

# plt.show()
print('he')


