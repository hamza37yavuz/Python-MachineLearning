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
print(cm)
