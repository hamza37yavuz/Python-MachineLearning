# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 15:53:31 2022

@author: HAMZA
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

veriler = pd.read_csv('Ads_CTR_optimisation.csv')
d,toplam=10,0
secilenler = []
for n in range(0,10000):
    ad = random.randrange(d)
    secilenler.append(ad)
    odul = veriler.values[n,ad] #verilerdeki n. satır 1 ise ödül
    toplam += odul
plt.hist(secilenler)
