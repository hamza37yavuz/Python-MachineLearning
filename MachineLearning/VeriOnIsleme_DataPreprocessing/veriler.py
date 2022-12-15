# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 18:01:01 2022

@author: HAMZA
"""
#bolum 3 ders 7
import pandas as pd

veriler = pd.read_csv('veriler.csv',)
print(veriler)

boykilo = veriler[['boy','kilo']]
print(boykilo)