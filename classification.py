import matplotlib.pyplot as plt
from sklearn.cluster import KMeans,AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler,MinMaxScaler
import pandas as pd 
import sys
import numpy as np
def Clustering_Vulnarebility(data,plotting=False):
        scale = MinMaxScaler()
        scale.fit(data)
        data= scale.transform(data)
        print(data)

        data[0] = 2*data[0]
        prediction = AgglomerativeClustering(n_clusters=3,linkage='ward').fit_predict(data)
        if plotting:
                plt.scatter(data.iloc[:, 0], data.iloc[:, 1], alpha =0.5,c=prediction, s=50, cmap='viridis')
                centers = kmeans.cluster_centers_
                plt.scatter(centers[:, 1], centers[:, 2], c='black', s=50, alpha=0)

        return prediction
def Clustering_Criticality(data,plotting=False):
        scale = MinMaxScaler()
        scale.fit(data)
        data= scale.transform(data)
        prediction = AgglomerativeClustering(n_clusters=3,linkage='ward').fit_predict(data)
        #prediction = clustering.fit_predict(data)
        if plotting:
                plt.scatter(data.iloc[:, 0], data.iloc[:, 1], alpha =0.5,c=prediction, s=50, cmap='viridis')
                centers = kmeans.cluster_centers_
                plt.scatter(centers[:, 1], centers[:, 2], c='black', s=50, alpha=0)
        return prediction
