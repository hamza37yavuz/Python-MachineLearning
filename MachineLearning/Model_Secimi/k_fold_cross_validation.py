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