# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 18:01:01 2022

@author: HAMZA
"""
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
import statsmodels.api as sm

#verileri alma
veriler = pd.read_csv('maaslar_yeni.csv')

#dataFrame icerisinden kullanilacak data
a = veriler.iloc[:,2:6]
#dataframe de bulunan verilerin birbiri ile iliskisini verir
print("\n")
print(veriler.corr())
print("\n")
#backward elimination
x=veriler.iloc[:,2:3]
x1 = pd.concat([veriler.iloc[:,2:3],veriler.iloc[:,4:5]], axis=1)
x2 = veriler.iloc[:,2:5]
y = veriler.iloc[:,5:6]
#convert NumPY array
X = x.values
Y = y.values
#%%
#***********************************************************
#lineer regresyon yapilirsa ne olur

from sklearn.linear_model import LinearRegression

deneme = LinearRegression()
deneme.fit(X,Y)
print("\nLINEAR REGRESSION OLS DEGERI")
model = sm.OLS(deneme.predict(X),X)
print(model.fit().summary())

#%%
#***********************************************************
#polynomial regression (nonlinear model) kutuphaneler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

#polynomial regression (nonlinear model) degree = 2
pol_reg = PolynomialFeatures(degree = 2)
x_pol = pol_reg.fit_transform(X)
lin_reg = LinearRegression()
lin_reg.fit(x_pol,y)
print("\nPOLYNOMIAL1 REGRESYON OLS DEGERI")
model2 = sm.OLS(lin_reg.predict(pol_reg.fit_transform(X)),X)
print(model2.fit().summary())

#us derecesini artirarak denememizi tekrarladik degree = 4
pol_reg = PolynomialFeatures(degree = 4)
x_pol = pol_reg.fit_transform(X)
lin_reg2 = LinearRegression()
lin_reg2.fit(x_pol,y)
print("\nPOLYNOMIAL2 REGRESYON OLS DEGERI")
model3 = sm.OLS(lin_reg2.predict(pol_reg.fit_transform(X)),X)
print(model3.fit().summary())
#%%
#Olcekleme (scale)
#***********************************************************
from sklearn.preprocessing import StandardScaler
sc1 = StandardScaler()
x_sc = sc1.fit_transform(X)
sc2 = StandardScaler()
y_sc = sc2.fit_transform(Y)
#***********************************************************
#%%
#SVR
from sklearn.svm import SVR
svr_reg = SVR(kernel="rbf")
svr_reg.fit(x_sc,y_sc)

print('\nSVR OLS DEGERI')
model4 = sm.OLS(svr_reg.predict(x_sc),x_sc)
print(model4.fit().summary())
#***********************************************************
#%%
#DECISION TREE (karar ağacı)
#burada verilerin hepsini bölmeler içine alarak ogrenir
#buradaogrenme tamamlandikta sonra X 0.5 artirilip tekrar grafik cizilmesi
#istenirse ayni grafik cizilir.
from sklearn.tree import DecisionTreeRegressor
r_dt = DecisionTreeRegressor(random_state=0)
r_dt.fit(X,Y)
print('\nDECISION TREE OLS DEGERI')
model5 = sm.OLS(r_dt.predict(X),X)
print(model5.fit().summary())
#***********************************************************
#%%
#RANDOM FOREST (çoklu karar agaclari)
from sklearn.ensemble import RandomForestRegressor
rf_reg = RandomForestRegressor(n_estimators = 10,random_state=0)
rf_reg.fit(X,Y.ravel())
#veri gorsellestirme

print('\nRANDOM FOREST OLS DEGERI')
model6 = sm.OLS(rf_reg.predict(X),X)
print(model6.fit().summary())