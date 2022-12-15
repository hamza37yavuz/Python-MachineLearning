# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 18:01:01 2022

@author: HAMZA
"""
#polinom regression sablon
import numpy as np
import pandas as pd

veriler = pd.read_csv('maaslar.csv',)
#dataFrame Slice
x = veriler.iloc[:,1:2]
y = veriler.iloc[:,2:]
#convert NumPY array
X = x.values
Y = y.values

#lineer regresyon yapilirsa ne olur
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
deneme = LinearRegression()
#dogrusal modeli gorsellestirme
deneme.fit(X,Y)
plt.scatter(X,Y)
plt.plot(X,deneme.predict(X),color="blue")

#polynomial regression (nonlinear model) kutuphaneler
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#polynomial regression (nonlinear model) degree = 2
pol_reg = PolynomialFeatures(degree = 2)
x_pol = pol_reg.fit_transform(X)
lin_reg = LinearRegression()
lin_reg.fit(x_pol,y)

#polinomal modeli gorsellestirme
plt.scatter(X,Y,color = "black")
plt.plot(X,lin_reg.predict(pol_reg.fit_transform(X)),color="red")

#us derecesini artirarak denememizi tekrarladik degree = 4
pol_reg = PolynomialFeatures(degree = 4)
x_pol = pol_reg.fit_transform(X)
lin_reg2 = LinearRegression()
lin_reg2.fit(x_pol,y)
plt.scatter(X,Y,color = "black")
plt.plot(X,lin_reg2.predict(pol_reg.fit_transform(X)),color="purple")

#tahminler
#eger linear regression yapilirsa
print(deneme.predict([[11]]))
print(deneme.predict([[6.6]]))
#eger polynomial regression yapilirsa
print(lin_reg2.predict(pol_reg.fit_transform([[11]])))
print(lin_reg2.predict(pol_reg.fit_transform([[6.6]])))

