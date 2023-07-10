#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import re
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix

#Cumlenin icerisindeki stop wordler uzaklastirilmalidir
    #durma = nltk.download('stopwords') 
ps = PorterStemmer()
nltk.download('stopwords') 

data = pd.read_csv('Restaurant_Reviews.csv')
sonuc = []
#PREPROCESSING
for i in range(1000):
    #Filtreleme Noktalama işaretlerini kaldirma
    data1 = re.sub('[^a-zA-Z]',' ',data["Review"][i])
    
    #Buyuk ve kucuk harfler farkli kelime ifade etmemeli
    data1 = data1.lower()
    
    #Her kelimeye indeks atamasi yapalim
    data1 = data1.split()
    
    #kelimenin kokunu bulacagiz ve burada stopwords'un elemesini yapacagiz
    data1 = [ps.stem(kelime) for kelime in data1 if not kelime in set(stopwords.words('english'))]
    
    #tekrar bunu bir string yapacagiz ve bir vektor sayiciyla sayacagiz
    data1 = ' '.join(data1)
    sonuc.append(data1)
#feture extraction oznitelik cikarimi
# BAG OF WORDS BOW
cv = CountVectorizer(max_features=2000)
x = cv.fit_transform(sonuc).toarray()
y = data.iloc[:,1].values

x_train, x_test, y_train, y_test, = train_test_split(x, y, test_size = 0.20, random_state = 0)

gnb = GaussianNB()
gnb.fit(x_train, y_train)

y_pred = gnb.predict(x_test)

cm = confusion_matrix(y_test, y_pred)
print(cm)