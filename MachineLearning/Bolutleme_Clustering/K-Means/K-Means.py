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