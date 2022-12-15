# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 15:29:30 2022

@author: HAMZA
"""
# Bolum 3
#------Prediction------
#Basit Lineer regresyon: verileri nokta gibi dusunursek
#   2 boyutlu uzayda verilere yakın bir dogru olusturma
#   olayi olarak adlandirabiliriz. Verileri basitlestirmeye calisiyoruz
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

#Verileri Hazırlama
veriler = pd.read_csv('satislar.csv')

aylar = veriler[['Aylar']]
satislar = veriler[['Satislar']]

x_train, x_test, y_train, y_test, = train_test_split(aylar, satislar, test_size = 0.33, random_state = 0)

sc = StandardScaler()
X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)

Y_train = sc.fit_transform(y_train)
Y_test = sc.fit_transform(y_test)

#Dogrusal Regresyon Modelini Insa Etmeye Baslanacak
lr = LinearRegression()
lr.fit(X_train,Y_train) #X_train i kullanarak Y_train'insa et

#Tahmin Degerelerini Alma
#Y_test degeri sisteme dahil edilmeden X_test verildi ve tahmin edilmesi istendi 
tahmin = lr.predict(X_test)

