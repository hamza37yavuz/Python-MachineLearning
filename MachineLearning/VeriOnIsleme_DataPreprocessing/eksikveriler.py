# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 18:01:01 2022

@author: HAMZA
"""
#bolum 3 ders 7
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

veriler = pd.read_csv('eksikveriler.csv',)
print(veriler)
print("\n")

#eksik veriler
imputer = SimpleImputer(missing_values=np.nan,strategy="mean")
Yas = veriler.iloc[:,1:4].values
print(Yas)
print("\n")

imputer = imputer.fit(Yas[:,1:4])#ogrenme
Yas[:,1:4] = imputer.transform(Yas[:,1:4]) #verileri doldurma
print(Yas)
 