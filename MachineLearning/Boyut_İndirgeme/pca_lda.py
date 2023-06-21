import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from sklearn.preprocessing import RobustScaler
from sklearn.model_selection import train_test_split
# Logistic Regression
from sklearn.linear_model import LogisticRegression
# PCA
from sklearn.decomposition import PCA
# Confusion Matrix
from sklearn.metrics import confusion_matrix

"""
RobustScaler, veri olceklendirme yontemlerinden biridir ve ozelliklerinizi olceklendirmenize yardimci olan bir veri donusturme aracidir. 
Ozellikle, olceklendirme yaparken aykiri degerlerin etkisini azaltmak istediginiz durumlarda kullanislidir.

RobustScaler, veri ozelliklerinin dagilimini ortalamaya ve standart sapmaya dayali olarak olceklendirmek yerine, medyan ve yuzdelik aralik kullanarak olçeklendirme gercekleştirir.
Bu nedenle, aykiri degerlerin medyan ve yuzdelik aralik uzerindeki etkisi minimize edilir.

RobustScaler, her bir ozellik icin medyan degeri ve yuzdelik araligi hesaplar. Medyan, veri noktalarinin orta noktasidir ve yuzdelik araligi, veri noktalarinin belirli yuzdeliklerini temsil eder.
Ardindan, her bir ozellik degeri icin medyani cikarir ve yuzdelik araliga boler, boylece ozellik degerlerini olceklendirir.

Bu islem sonucunda, veri ozellikleri arasinda dagilim farklari azalir ve ayni olcekte olurlar. Bu, ozellikleri birbirleriyle karsilastirmak veya makine ogrenimi modellerine beslemek icin daha uygun bir hale getirir. 
Ayrica, aykiri degerlerin etkisini azaltmak için kullanildigindan, RobustScaler, verilerinizde aykiri degerlerin bulundugu durumlarda daha saglam sonuclar uretir.
"""
rc = RobustScaler()

veriler = pd.read_csv('Wine.csv')
# Sarapların 13 farklı ozelligi oldugunu gorduk
x = veriler.iloc[:, 0:13].values
y = veriler.iloc[:, 13].values

# Elde ettiigimiz verileri train test seklinde ayiralim

x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=0.2, random_state=0)


X_train = rc.fit_transform(x_train)
X_test = rc.fit_transform(x_test)

# PCA 
# 13 boyut n boyuta indirgenecek
pca = PCA(n_components=2)
# fit islemi bir kez yapilir diger veri parcalari sadece transform edilir. 
X_train2 = pca.fit_transform(X_train)
X_test2 = pca.transform(X_test)
# pca donusumunden gelen logistic regression
classifier = LogisticRegression(random_state=0)
classifier.fit(X_train2,y_train)
# pca donusumu yapilmamis veriler icin logistic regression
classifier2 = LogisticRegression(random_state=0)
classifier2.fit(X_train,y_train)
# Tahmin ettirelim
# PCA
y_pred = classifier.predict(X_test2)
# NORMAL
y_pred2 = classifier2.predict(X_test)

print("PCA\n")
cm = confusion_matrix(y_test,y_pred)
print(cm)

print("\n\nNORMAL\n")
cm2 = confusion_matrix(y_test,y_pred2)
print(cm2)

print("\n\nCOMPARE\n")
cm2 = confusion_matrix(y_pred,y_pred2)
print(cm2)

# Burada PCA basariyi artirmadi ama verileri 13 ten iki sutuna indirmesine ragmen iyi calisti.
# Bazi durumlarda basariyi artiradabilir

# Benzer islemleri LDA icin yapalim
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
lda = LDA(n_components=2)
# Burada pca ile lda nin en onemli farki goruluyor.
# lda siniflari da ogrenmesi icin y_train sutununu da parametre olarak aliyor
X_train3 = lda.fit_transform(X_train,y_train)
X_test3 = lda.transform(X_test)
# lda donusumunden gelen logistic regression
classifier3 = LogisticRegression(random_state=0)
classifier3.fit(X_train3,y_train)

y_pred3 = classifier.predict(X_test3)

print("\n\nLDA\n")
cm4 = confusion_matrix(y_test,y_pred)
print(cm4)
# bu veri setinde lda ile pca arasinda bir fark olmadigi zannedilşebilir.
# scaler degistirerek burada fark var mi diye bakilabilir.
# farkli veri sseti ile deneyerek fark daha net bir sekilde gorulebilir.

