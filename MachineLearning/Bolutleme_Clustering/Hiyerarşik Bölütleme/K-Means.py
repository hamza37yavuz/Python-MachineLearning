# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 17:25:50 2022

@author: HAMZA
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

veriler = pd.read_csv("musteriler.csv")
# hacim : yaptigi alisveris hacmi
X = veriler.iloc[:,3:]
#gorsellestirme icin iki kolonu aldik

#K-MEANS
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3,init = 'k-means++')
kmeans.fit(X)
print(kmeans.cluster_centers_)
#k için optimum deger bulma

sonuclar = []
for i in range(1,10):
    kmeans = KMeans(n_clusters=i,init = 'k-means++',random_state=123)
    kmeans.fit(X)
    sonuclar.append(kmeans.inertia_)
plt.plot(range(1,10), sonuclar)
plt.title("KM")
plt.show()

#HC Hiyerarşik bölütleme
from sklearn.cluster import AgglomerativeClustering

ac = AgglomerativeClustering(n_clusters=3,affinity="euclidean",linkage="ward")
yPred = ac.fit_predict(X)
print(yPred)

plt.scatter(X[yPred == 0,0], X[yPred == 0,1],s = 100,c = "red")
plt.scatter(X[yPred == 1,0], X[yPred == 1,1],s = 100,c = "blue")
plt.scatter(X[yPred == 2,0], X[yPred == 2,1],s = 100,c = "green")
plt.scatter(X[yPred == 3,0], X[yPred == 3,1],s = 100,c = "green")
plt.title('HC')
plt.show()

import scipy.cluster.hierarchy as sch
dendogram = sch.dendrogram(sch.linkage(X,method='ward'))
plt.show()




