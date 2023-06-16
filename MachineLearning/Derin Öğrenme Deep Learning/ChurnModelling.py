# -*- coding: utf-8 -*-
"""
Created on Mon june  3 18:01:01 2023

@author: HAMZA
"""
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
# Yapay sinir agi icin kutuphaneleri ekleyelim 
import keras
from keras.models import Sequential
from keras.layers import Dense
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
from sklearn.model_selection import train_test_split

x_train, x_test,y_train,y_test = train_test_split(X,Y,test_size=0.33, random_state=0)

# verilerin olceklenmesi Simdilik standart scaler yaptik

sc = StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)
# print(X)

# giris katmanimizda 13 adet sutun var bu sutunlar yardimiyla sonuca 1'e indirilecek

# Yapay sinir agi olusturalim 
classifier = Sequential() #yapay sinir agini olusturduk
# kac noron olacak -units- e bagli
# sinapslar nasıl initialize edilecek 0 ayakın olmali ama 0 olmamali
# activation function ne olacak biz relu dedik
# giristeki katmanda ne var
# 6 norondan olusan gizli katman olusturalım
classifier.add(Dense(units=6,kernel_initializer = "glorot_uniform",activation="relu",input_dim=11,))

# 6 norondan olusan bir gizli katman daha olusturalım
classifier.add(Dense(units=6,kernel_initializer = "glorot_uniform",activation="relu"))

# cikis katmanini olusturalim
classifier.add(Dense(units=1,kernel_initializer = "glorot_uniform",activation="sigmoid"))

# suan giris katmaninda 11 noron bulunuyor 
# 2 tane gizli katman var bu katmanların her biri 6 norondan olusuyor
# 1 tane cikis katmani olusturduk

# adam optimizerini varsayilan degiskenler ile kullanacagiz
# loss fonksiyonu nasil kullanilir ne yapar kayıp degerini nasil bulacagimizi fonksiyon tanımlamaliyiz.
# loss fonksiyonu kaybımızın ne oldugunu tespit etmemize yardim eder
# neyi optimize edecegimizi sinir agina belirtmeliyiz. bu ornekte accuracy yazacagiz
classifier.compile(optimizer="adam",loss="binary_crossentropy",metrics=["accuracy"])  

# klasik fit transfom islemini yapacagiz
# Sadece parametre farklari var batch_size ve epoch degerlerini biz burada verecegiz
# epochs kaç aşamada ogrenecegini soyler.
# batch_size verileri kaçarli gruplayarak egitim surecine tabi tutacagini belirtir. varsayilan olarak 32 dir.
classifier.fit(X_train,y_train,epochs=50,batch_size=32)

y_pred = classifier.predict(X_test)
print(y_pred)

y_pred = (y_pred>0.5)
cm = confusion_matrix(y_test,y_pred)
print(cm)
