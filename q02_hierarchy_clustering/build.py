# %load q02_hierarchy_clustering/build.py
# Default imports

import pandas as pd
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from sklearn.preprocessing import scale
from scipy.cluster import hierarchy
from sklearn import datasets

digits = datasets.load_digits()
df = pd.DataFrame(scale(digits.data), index=digits.target)

# Write your solution here :
def hierarchy_clustering(df):
    Z_avg = linkage(df, 'average') 
    Z_single = linkage(df, 'single') 
    Z_complete = linkage(df, 'complete') 
    Z_ward = linkage(df, 'ward') 

    plt.figure(figsize=(15, 10))
    plt.subplot(411)
    dendrogram(
        Z_avg,
        leaf_rotation=90.,  
        leaf_font_size=3., 
    )
    plt.title('Average')

    plt.figure(figsize=(15, 10))
    plt.subplot(412)
    dendrogram(
        Z_single,
        leaf_rotation=90.,  
        leaf_font_size=3.,  
    )
    plt.title('Single')

    plt.subplot(413)
    dendrogram(
        Z_complete,
        leaf_rotation=90.,  
        leaf_font_size=3.,  
    )
    plt.title('Complete')

    plt.subplot(414)
    dendrogram(
        Z_ward,
        leaf_rotation=90.,  
        leaf_font_size=3.,  
    )
    plt.title('Ward')
    plt.xlabel('sample index')
    plt.ylabel('distance')

    plt.show()

