import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from sklearn.preprocessing import RobustScaler
from sklearn.model_selection import train_test_split

sc = RobustScaler()

veriler = pd.read_csv('Wine.csv')
# Sarapların 13 farklı ozelligi oldugunu gorduk
x = veriler.iloc[:, 0:13].values
y = veriler.iloc[:, 13].values

# Elde ettiigimiz verileri train test seklinde ayiralim

x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=0.2, random_state=0)


X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)
