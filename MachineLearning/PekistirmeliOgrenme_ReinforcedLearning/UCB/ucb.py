# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 15:53:31 2022

@author: HAMZA

Adım 1 : Her turda tur sayısı = n her reklam altaernatifi için
aşağıdaki değerler tutulur
Ni(n) = i sayılı reklamın o ana kadarki tıklanma sayısı
Ri(n) = o ana kadar ki i reklamından gelen toplam ödül
Adım 2: yukarıdaki iki sayıdan aşağıdaki değerler hesaplanır
o ana kadarki her reklamın ortalama ödülü Ri(n)/Ni(n)
güven aralığı d(n)karekökk3logn/2Ni(n) 
Adım 3 : en yüksek ucb değerine sahip olanı alırız

"""
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
veriler = pd.read_csv('Ads_CTR_Optimisation.csv')

"""
for n in range(0,10000):
    ad,maxUcb = 0,0
    
    for i in range (0,d):
        if veriler[n][i] > 1:
            tiklamalar[i] += 1
            ortalama = oduller[i]/tiklamalar[i]
             
        if maxUcb<ucb:
            ucb = maxUcb
            ad = i
"""
N = 10000 # 10.000 tıklama
d = 10  # toplam 10 ilan var
#Ri(n)
oduller = [0] * d #ilk basta butun ilanların odulu 0
#Ni(n)
tiklamalar,destek = [0] * d, [0] * d #o ana kadarki tıklamalar
toplam = 0 # toplam odul
secilenler = []
for n in range(1,N):
    ad,a = 0,0 #seçilen ilan
    max_ucb = 0
    for i in range(0,d):
        if(tiklamalar[i] > 0):
            ortalama = oduller[i] / tiklamalar[i]
            delta = math.sqrt(3/2* math.log(n)/tiklamalar[i])
            
            ucb = ortalama + delta
        else:
            secilenler.append(ad)
            tiklamalar[ad] = tiklamalar[ad]+ 1
            odul = veriler.values[n,ad] # verilerdeki n. satır = 1 ise odul 1
            oduller[ad] = oduller[ad]+ odul
            toplam = toplam + odul
            a=1
            break
        if max_ucb < ucb: #max'tan büyük bir ucb çıktı
            max_ucb = ucb
            ad = i 
    if(a==1):
        break        
    secilenler.append(ad)
    tiklamalar[ad] = tiklamalar[ad]+ 1
    odul = veriler.values[n,ad] # verilerdeki n. satır = 1 ise odul 1
    oduller[ad] = oduller[ad]+ odul
    toplam = toplam + odul
print('Toplam Odul:')   
print(toplam)

plt.hist(secilenler)
plt.show()        
            
            