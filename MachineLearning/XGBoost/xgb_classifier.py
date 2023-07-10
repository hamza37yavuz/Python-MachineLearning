# -*- coding: utf-8 -*-
"""
Created on Mon june  3 18:01:01 2023

@author: HAMZA
"""
import pandas as pd
from sklearn import preprocessing
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix

#XGBOOST
from xgboost import XGBClassifier

# 2.1 veri yukleme
veriler = pd.read_csv('Churn_modelling.csv')

# print(veriler)

# 2. veri on isleme
X = veriler.iloc[:,3:13].values
Y = veriler.iloc[:,13].values

# Ulke isimleri 0 ve 1 seklinde ifade edilmelidir encode edelim
le = preprocessing.LabelEncoder()
X[:,1] = le.fit_transform(X[:,1])
# Cinsiyet 0 ve 1 seklinde ifade edilmelidir encode edelim
le2 = preprocessing.LabelEncoder()
X[:,2] = le.fit_transform(X[:,2])
ohe = ColumnTransformer([("ohe", OneHotEncoder(dtype=float),[1])],
                        remainder="passthrough"
                        )
X = ohe.fit_transform(X)
X = X[:,1:]

#verilkkerin egitim ve test icin bolunmesi
x_train, x_test,y_train,y_test = train_test_split(X,Y,test_size=0.33, random_state=0)


sc = StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)

xgbc = XGBClassifier()
xgbc.fit(X_train,y_train)

y_pred = xgbc.predict(X_test)

cm = confusion_matrix(y_pred=y_pred,y_true=y_test)
