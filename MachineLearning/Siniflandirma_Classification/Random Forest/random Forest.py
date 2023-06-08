# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 18:01:01 2022

@author: HAMZA
"""
#bolum 3 kutuphaneler
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#2. veri on isleme
#2.1 veri yukleme
veriler = pd.read_csv('veriler.csv')
#Cocuklar Cikarilmazsa
x = veriler.iloc[:,1:4].values
y = veriler.iloc[:,4:5].values

#Cocuklar Cikarilirsaa
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

#Logistic Regression
from sklearn.linear_model import LogisticRegression
logR = LogisticRegression(random_state=0)
logR.fit(X_train,y_train)
yPred = logR.predict(X_test)
print(yPred)

#confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, yPred)
print("\nLOGISTIC")
print(cm)

from sklearn.neighbors import KNeighborsClassifier
#eger n_neigbors düşürülürse başarı artar
knn = KNeighborsClassifier(n_neighbors=5,metric = "minkowski")
knn.fit(X_train,y_train)
yPred = knn.predict(X_test)
cm = confusion_matrix(y_test, yPred)
print("\nKNN")
print(cm)

from sklearn.svm import SVC
svc = SVC(kernel="rbf")
svc.fit(X_train,y_train)
yPred = svc.predict(X_test)
cm = confusion_matrix(y_test, yPred)
print("\nSVC")
print(cm)

#gaussian naive bayes 
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

#Decision Tree CRITERION
from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier(criterion="entropy")
dtc.fit(X_train,y_train)
yPred = dtc.predict(X_test)
cm = confusion_matrix(y_test, yPred)
print("\nDECISISON TREE") 
print(cm)

#Random Forest 
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=5,criterion="entropy")
rfc.fit(X_train,y_train)
yPred = rfc.predict(X_test)
cm = confusion_matrix(y_test, yPred)
print("\nRANDOM FOREST") 
print(cm)
