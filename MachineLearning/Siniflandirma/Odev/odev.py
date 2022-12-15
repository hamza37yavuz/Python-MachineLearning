# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 18:01:01 2022

@author: HAMZA
"""
#bolum 3 kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import datasets

#Veriyi Gorsellestirelim
iris = datasets.load_iris()
X = iris.data[:,:2]
y = iris.target
xmin,xmax = X[:,0].min() - .5,X[:,0].max() + .5
ymin,ymax = X[:,1].min() - .5,X[:,1].max() + .5
plt.figure(2,figsize=(8,6))
plt.clf()
#plot training points
plt.scatter(X[:,0],X[:,1], c=y,cmap=plt.cm.Set1,edgecolor = "k")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.xticks(())
plt.yticks(())

#2. veri on isleme
#2.1 veri yukleme
veriler = pd.read_excel('iris.xls')
#Cocuklar Cikarilmazsa
x = veriler.iloc[:,0:4].values
y = veriler.iloc[:,4:5].values

# Sistemi Temsil Etmeyen Degerler Cikarildi
"""
x = veriler.iloc[5:,1:4].values
y = veriler.iloc[5:,4:5].values
"""
#2.6 veri setini train ve test olarak ayirma
x_train, x_test, y_train, y_test, = train_test_split(x, y, test_size = 0.33, random_state = 0)

#2.7 veri setindeki verileri olcekleme 
sc = StandardScaler()
X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)

#Siniflandirma Algoritmalari

#1-Logistic Regression
from sklearn.linear_model import LogisticRegression
logR = LogisticRegression(random_state=0)
logR.fit(X_train,y_train)
yPred = logR.predict(X_test)
print(yPred)

#confusion matrix Karmasiklik Matrisi
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, yPred)
print("\nLOGISTIC")
print(cm)

#2-KNN Algoritmasi
from sklearn.neighbors import KNeighborsClassifier
#eger n_neigbors düşürülürse başarı artar
knn = KNeighborsClassifier(n_neighbors=5,metric = "minkowski")
knn.fit(X_train,y_train)
yPred = knn.predict(X_test)
cm = confusion_matrix(y_test, yPred)
print("\nKNN")
print(cm)

#3-SVC Support Verctor Classifyer 
from sklearn.svm import SVC
svc = SVC(kernel="rbf")#burada farkli kerneller kullanilabilir
svc.fit(X_train,y_train)
yPred = svc.predict(X_test)
cm = confusion_matrix(y_test, yPred)
print("\nSVC")
print(cm)

#Gaussian Naive Bayes BURADA GAUSSIAN YERINE BASKA BİR FONKSIYON KULLANILABİLİR 
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(X_train,y_train)
yPred = gnb.predict(X_test)
cm = confusion_matrix(y_test, yPred)
print("\nGNB")
print(cm)

#Multinominal Naive Bayes 
#kodun calismasi icin degerler veri icerisinde olmamalidir
"""
from sklearn.naive_bayes import MultinomialNB
mnb = MultinomialNB()
mnb.fit(X_train,y_train)
yPred = mnb.predict(X_test)
cm = confusion_matrix(y_test, yPred)
print("\nMNB")
print(cm)
"""

#5-Decision Tree CRITERION fonksiyonu ile oyananabilir.
from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier(criterion="entropy")
dtc.fit(X_train,y_train)
yPred = dtc.predict(X_test)
cm = confusion_matrix(y_test, yPred)
print("\nDECISISON TREE") 
print(cm)

#6-Random Forest 
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=5,criterion="entropy")
rfc.fit(X_train,y_train)
yPred = rfc.predict(X_test)
cm = confusion_matrix(y_test, yPred)
print("\nRANDOM FOREST") 
print(cm)
print("\n")
#ihitimaller dizisi
yProba =  rfc.predict_proba(X_test)
print(yProba)

#AUC ve ROC la ilgili scikitlearn den bakabilirsin
#roc metrikleri için kullanilan bolum
from sklearn import metrics
fpr,tpr,thold = metrics.roc_curve(y_test,yProba[:,0],pos_label="e")
"""
print(tpr)
print("\n")
print(fpr)
print("\n")
print(thold)
"""
