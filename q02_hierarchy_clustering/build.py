# %load q02_hierarchy_clustering/build.py
# Default imports

import pandas as pd, numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from sklearn.preprocessing import scale
from scipy.cluster import hierarchy
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn import datasets

digits = datasets.load_digits()
df = pd.DataFrame(scale(digits.data), index=digits.target)

def hierarchy_clustering(df):
    Zc = linkage(df, 'complete')
    Za = linkage(df, 'average')
    Zs = linkage(df, 'single')
    Zw = linkage(df, 'ward')
    plt.figure(figsize=(20,10))
    plt.locator_params(nbins=10)
    plt.subplot(141)
    plt.title('Complete Linkage')
    dendrogram(Zc,p=20, truncate_mode='lastp',leaf_rotation=90, leaf_font_size=8)
    plt.subplot(142)
    plt.title('Average Linkage')
    dendrogram(Za,p=20, truncate_mode='lastp',leaf_rotation=90, leaf_font_size=8)
    plt.subplot(143)
    plt.title('Single Linkage')
    dendrogram(Zs,p=20, truncate_mode='lastp',leaf_rotation=90, leaf_font_size=8)
    plt.subplot(144)
    plt.title('Ward Linkage')
    dendrogram(Zw,p=20, truncate_mode='lastp',leaf_rotation=90, leaf_font_size=8)
    plt.tight_layout()
    plt.show();




