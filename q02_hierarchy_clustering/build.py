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


# Write your solution here :
def hierarchy_clustering(df):
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize=(50, 18))

    for linkage, cluster, ax in zip(
            [hierarchy.complete(df), hierarchy.average(df), hierarchy.single(df), hierarchy.ward(df)],
            ['c1', 'c2', 'c3', 'c4'],
            [ax1, ax2, ax3, ax4]):
        cluster = hierarchy.dendrogram(linkage, labels=df.index, p=12, truncate_mode="lastp", orientation='top',
                                       color_threshold=0, leaf_font_size=10, distance_sort=True, ax=ax)
    ax1.set_title('Complete Linkage')
    ax2.set_title('Average Linkage')
    ax3.set_title('Single Linkage')
    ax4.set_title('Ward')
    plt.show()
