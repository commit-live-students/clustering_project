# %load q02_hierarchy_clustering/build.py
# Default imports

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from scipy.cluster import hierarchy
from sklearn import datasets

digits = datasets.load_digits()
df = pd.DataFrame(scale(digits.data), index=digits.target)

# Write your solution here :
def hierarchy_clustering (df):
    D=hierarchy.linkage(df,'average')
    plt.figure(figsize=(25,10))
    plt.title("Hierarchial clustering dendogram")
    plt.xlabel('sample index')
    plt.ylabel('distance')
    hierarchy.dendogram(D,leaf_rotation=90.,leaf_font_size=8.)
    plt.show()
#hierarchy_clustering (df)
