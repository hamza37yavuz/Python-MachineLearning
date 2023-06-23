#1. kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# veri kumesi
dataset = pd.read_csv('Social_Network_Ads.csv')
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, 4].values

# egitim ve test kumelerinin bolunmesi
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Olcekleme
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# SVM Support Vector Classifier
from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf', random_state = 0)
classifier.fit(X_train, y_train)

# Tahminler
y_pred = classifier.predict(X_test)

#  Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

print(cm)


#k-katlamali capraz dogrulama 
from sklearn.model_selection import cross_val_score as cvs
''' 
1. estimator : classifier (bizim durum) Hangi algoritmayi kullanacagi
2. X hangi X degerinden 
3. Y hangi y degerini bulacagi 
4. cv : kaç katlamali

'''
basari = cvs(estimator = classifier, X=X_train, y=y_train , cv = 4)
print(basari.mean()) 
print(basari.std()) # standart sapmalari bulacak

# Parametrelerin optimize edilmesi
from sklearn.model_selection import GridSearchCV
# Verecegimiz parametrelerin farklı yapilarda olması gerekebilir.
# Burada sozlük yapisi icerisinde parametreleri alacagiz
# Sozluk olusturma sirasinda baby step ya da giant step gibi kavramlar vardir.
# Grid search brute force olarak calisir ve bu searchi optimize etmek icin bu kavramlar kullanilir.
# Ornegin dev adimlari once buyuk sayilar denenir 0 500 1000 gibi sonra hangi araligin daha uygun olduguna karar vererek ilerlenir.


p = [{'C':[1,2,3,4,5],'kernel':['linear']},
     {'C':[1,10,100,1000],'kernel':['rbf'], 'gamma':[1,0.5,0.1,0.01,0.001]}]

''' 
1. estimator : classifier (bizim durum) neyi optimize ediyoruz
2. param_grid: denenecek parametreler 
3. scoring: neye göre scorlanacak ornegin accuracy (recall .etc)
4. cv: kaç fold olacak
5. n_jobs: Ayni anda calisacak is sayisi
'''

gs = GridSearchCV(estimator = classifier,
                  param_grid = p,
                  scoring = 'accuracy',
                  cv = 10,
                  n_jobs=-1)
# svm'in uzerine bir kilif geciriyoruz. Cekirdekte SVM calisacak ama bunu grid search ile beraber tekrarlayacak.
grid_search = gs.fit(X_train,y_train)
# Amacimiz en iyi parametreleri bulmakti.
the_best_score = grid_search.best_score_
the_best_params =  grid_search.best_params_

print(the_best_score) 
print(the_best_params)
