import pandas as pd
import pickle as pck
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

url = "https://bilkav.com/satislar.csv"
veriler = pd.read_csv(url)
veriler = veriler.values
X = veriler[:,0:1]
Y = veriler[:,1]
X_train, x_test, Y_train, y_test, = train_test_split(X, Y, test_size = 0.33, random_state = 0)

# lr = LinearRegression() 

# lr.fit(X_train,Y_train)
# print(lr.predict(x_test))

dosyaIsmi = "model"
# pck.dump(lr,open(dosyaIsmi,'wb')) # model kaydedildi

dosyaModel = pck.load(open(dosyaIsmi,'rb')) 
print(dosyaModel.predict(x_test))

