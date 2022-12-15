#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 19:03:45 2018

@author: sadievrenseker
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
veriler = pd.read_csv('Ads_CTR_Optimisation.csv')


#Thompson
N = 10000 # 10.000 tıklama
d = 10  # toplam 10 ilan var
#Ri(n)
#Ni(n)
birler,sifirlar = [0] * d,[0] * d #o ana kadarki tıklamalar
toplam = 0 # toplam odul
secilenler = []
for n in range(1,N):
    ad = 0 #seçilen ilan
    maxTh = 0
    for i in range(0,d):
        rasBeta = random.betavariate(birler[i]+1,sifirlar[i]+1)
        if(rasBeta>maxTh):
            maxTh = rasBeta
            ad = i
    secilenler.append(ad)
    odul = veriler.values[n,ad] # verilerdeki n. satır = 1 ise odul 1
    if(odul == 1):
        birler[ad] += 1
    else:
        sifirlar[ad] += 1
    toplam = toplam + odul
print('Toplam Odul:')   
print(toplam)

plt.hist(secilenler)
plt.show()







