# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 18:01:01 2022

@author: HAMZA
"""
#
import pandas as pd
from sklearn.metrics import r2_score

#verileri alma
veriler = pd.read_csv('maaslar.csv')
#dataFrame Slice
x = veriler.iloc[:,1:2]
y = veriler.iloc[:,2:]
#convert NumPY array
X = x.values
Y = y.values
#%%
#***********************************************************
#lineer regresyon yapilirsa ne olur
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
deneme = LinearRegression()
deneme.fit(X,Y)
#dogrusal modeli gorsellestirme
"""
plt.scatter(X,Y)
plt.plot(X,deneme.predict(X),color="blue")
"""
print("LINEAR REGRESYON R2 DEGERI")
print(r2_score(Y,deneme.predict(X)))
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
#polinomal modeli gorsellestirme
"""
plt.scatter(X,Y,color = "black")
plt.plot(X,lin_reg.predict(pol_reg.fit_transform(X)),color="red")
"""
print("POLYNOMIAL REGRESYON R2 DEGERI")
print(r2_score(Y,lin_reg.predict(pol_reg.fit_transform(X))))
#us derecesini artirarak denememizi tekrarladik degree = 4
pol_reg = PolynomialFeatures(degree = 4)
x_pol = pol_reg.fit_transform(X)
lin_reg2 = LinearRegression()
lin_reg2.fit(x_pol,y)
#polinomal modeli gorsellestirme
"""
plt.scatter(X,Y,color = "black")
plt.plot(X,lin_reg2.predict(pol_reg.fit_transform(X)),color="purple")
"""
print("POLYNOMIAL REGRESYON R2 DEGERI")
print(r2_score(Y,lin_reg2.predict(pol_reg.fit_transform(X))))
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
"""
plt.scatter(x_sc,y_sc,color = "blue")
plt.plot(x_sc,svr_reg.predict(svr_reg.predict(x_sc)),color="red")
plt.show()
"""
print('SVR R2 DEGERI')
print(r2_score(y_sc, svr_reg.predict(x_sc)))
#***********************************************************
#%%
#DECISION TREE (karar ağacı)
#burada verilerin hepsini bölmeler içine alarak ogrenir
#buradaogrenme tamamlandikta sonra X 0.5 artirilip tekrar grafik cizilmesi
#istenirse ayni grafik cizilir.
from sklearn.tree import DecisionTreeRegressor
r_dt = DecisionTreeRegressor(random_state=0)
r_dt.fit(X,Y)
"""
plt.scatter(X, Y, color='red')
plt.plot(X,r_dt.predict(X),color='blue')
"""
print('DECISION TREE R2 DEGERI')
print(r2_score(Y, r_dt.predict(X)))
#***********************************************************
#%%
#RANDOM FOREST (çoklu karar agaclari)
from sklearn.ensemble import RandomForestRegressor
rf_reg = RandomForestRegressor(n_estimators = 10,random_state=0)
rf_reg.fit(X,Y.ravel())
#veri gorsellestirme
plt.scatter(X,Y,color='red')
plt.plot(X,rf_reg.predict(X),color='blue')
plt.show()
print('RANDOM FOREST R2 DEGERI')
print(r2_score(Y, rf_reg.predict(X)))
