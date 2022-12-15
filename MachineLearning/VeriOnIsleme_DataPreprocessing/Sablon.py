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
veriler = pd.read_csv('eksikveriler.csv')

#2.2 veriden herhangi bir sutun degerlerini alma
ulke = veriler.iloc[:,0:1].values

#2.3 eksik verilerin yerini doldurma
imputer = SimpleImputer(missing_values=np.nan,strategy="mean")
yas = veriler.iloc[:,1:4].values
imputer = imputer.fit(yas[:,1:4])#ogrenme
yas[:,1:4] = imputer.transform(yas[:,1:4]) #verileri doldurma

#2.4 verinin bir sutununu islemeye hazir hale getirme
le = preprocessing.LabelEncoder()
ulke[:,0] = le.fit_transform(veriler.iloc[:,0])
#2.4.1 one hot encoder
ohe = preprocessing.OneHotEncoder()
ulke = ohe.fit_transform(ulke).toarray()

sonuc = pd.DataFrame(data = ulke,index = range(22),columns = ['fr','tr','us'])
sonuc2 = pd.DataFrame(data = yas, index = range(22) ,columns = ['boy','kilo','yas'])

cinsiyet = veriler.iloc[:,-1]
sonuc3 = pd.DataFrame(data = cinsiyet,index = range(22),columns = ['cinsiyet'])

#2.5 farkli sutunlar olarak alinan data frameleri birlestirme
s = pd.concat([sonuc,sonuc2],axis = 1)
s2 = pd.concat([s,sonuc3],axis = 1)

#2.6 veri setini train ve test olarak ayirma
x_train, x_test, y_train, y_test, = train_test_split(s, sonuc3, test_size = 0.33, random_state = 0)

#2.7 veri setindeki verileri olcekleme 
sc = StandardScaler()
X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)