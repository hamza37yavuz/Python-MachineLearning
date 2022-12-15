import numpy as np
import pandas as pd

# YENI SERI OLUSTURMA
# Sozluk yapisi ile Serie olusturma
isim_yas = {"Hamza" : 20, "Sinan" : 30, "Samet" : 40}
print(pd.Series(isim_yas))
# Liste kullanarak Serie olusturma
yas = [20,30,40]
isim = ["Hamza","Sinan","Samet"]
print(pd.Series(data = yas,index = isim))
# numpy dizisi ile Serie olusturma 
dizi = np.array(yas)
print(pd.Series(data = dizi))
print("\n")

# FARKLI SEKILLERDE FARKLI DEGERLERI ICEREN SERILER OLUSTURMAK
print(pd.Series(["A","B","C"],["Hamza","Ahmet","Cem"]))# hem index hem içerik string
nots = pd.Series([95,80,75],["Hamza","Ahmet","Cem"])
nots2 = pd.Series([75,90,65],["Hamza","Ahmet","Cem"])
print(nots+nots2)
print("\n")
# Serie nin icinden eleeman cagirma
print(nots2["Cem"])
print("\n")
# indis degeri bir y-tarafta var ama diger tarafta yoksa ne olur
nots = pd.Series([20,30,40,50],["a","b","c","d"])
nots2 = pd.Series([20,30,40,50],["a","f","g","c"])
print(nots+nots2)
print("\n")

# DATA FRAME PANDAS
print("-------------DATA FRAME PANDAS----------")
print("\n")
# TANITIM
data = np.random.randn(4,3)
dataFrame = pd.DataFrame(data)
print(dataFrame)
print(type(dataFrame))
print("\n")

# YENİ SATIR VE SUTUN EKLEME
newDataFrame = pd.DataFrame(data,index = ["Hamza","Samet","Umut","Hatice"], columns = ['Maas','Yas','Calisma Saati'])
print(newDataFrame)
print(newDataFrame[['Maas','Yas']]) # maas ve yas kolonlarini verir
print("\n")
# Data frame icerisinden bir degeri alma
print(newDataFrame.loc['Hamza'])
print("\n")
# Burada emeklilik sutunu eklenmis oldu
newDataFrame['Emeklilik'] = newDataFrame['Yas'] + newDataFrame['Yas']
print(newDataFrame)
print("\n")

# SUTUN VEYA SATIRI YOK ETME
print(newDataFrame.drop('Emeklilik',axis = 1)) # axis=1 ise sutunlar arasi kiyaslama yapar
print(newDataFrame.drop('Hamza',axis = 0)) # axis=0 ise satirlar arasi kiyaslama yapar
print(newDataFrame) # dropla attigimiz sutun tekrar geri geldi dropla bu sekilde temelli bir silme islemi yapilmaz
print("\n")
newDataFrame.drop('Emeklilik',axis = 1,inplace = True) # inplace = True ise verilen sutun geri gelmeyecek sekilde silinir
print(newDataFrame) # yukaridaki islemin aynisi satir icin de yapilabilir
print("\n")

# .loc FONKSİYONU ILE VERILERE ULASMA
print(newDataFrame.loc['Hamza']['Calisma Saati'])
print(newDataFrame.loc['Hamza','Calisma Saati'])
print("\n")

# DATA FRAME'LERİ BOOLEAN DEGERLERE DONUSTURMEK
print(newDataFrame < 0)
print(newDataFrame[newDataFrame < 0])
print(newDataFrame[newDataFrame["Yas"] > 0])
print("\n")

# INDEKS DEGISTIRMEK
print(newDataFrame.reset_index()) #temelli degistirmek istiyorsan inplace=True yazman gerekir 
print(newDataFrame)
new_index = ['Ham','Sam','Um','Hat']
newDataFrame['Yeni Indeks'] = new_index
print(newDataFrame)
print(newDataFrame.set_index('Yeni Indeks',inplace=True))#temelli degistirmek istiyorsan inplace=True yazman gerekir 
print(newDataFrame.loc['Ham'])

# MULTI INDEKS
indeks1 = ['ilkokul','ilkokul','ortaokul','ortaokul']
indeks2 = ['Hamza','Ahmet','Hasan','Samet']
multi = list(zip(indeks1,indeks2))
print(multi) # iki indeks eslesicek sekilde oldu
print(type(multi)) # burada tipine bakalim

# Data Frame icin liste yapısında ziplediğimiz indeks1 ve indeks2 hazirlanma asamasi
multi = pd.MultiIndex.from_tuples(multi) 
print(multi)
print(type(multi)) # ! tipi degisti 
# diger sutun verilerini liste seklinde olusturuyoruz sonra array'e ceviriyoruz
liste = np.array([[2,282],[1,374],[3,211],[4,202]])
# simdi data Frame olusturalim 
newDataFrame = pd.DataFrame(liste,index = multi,columns=['Sinif','Numara'])
print(newDataFrame)
#simdi bu data frame icindeki verilere nasil erisecegimize bakalim
print(newDataFrame.loc['ilkokul'])
print(newDataFrame.loc['ortaokul'])
print("\n")
print(newDataFrame.loc['ilkokul'].loc['Hamza'])
print("\n")
print(newDataFrame.loc['ortaokul'].loc['Samet'])

# -- PANDAS OPERASYONLAR --
# Bos Veriler (silinmesi ya da doldurulmasi gereken veriler)
# ilk olarak data frameleri olusturalim
havaDurumu = {"Istanbul":[30,29,np.nan],"Izmir":[40,39,38],"Ankara":[20,np.nan,25]}
havaDurumu = pd.DataFrame(havaDurumu)
havaDurumu2 = {"Istanbul":[30,29,np.nan],"Izmir":[40,39,38],"Ankara":[20,np.nan,25],"Antalya":[36,np.nan,np.nan]}
havaDurumu2 = pd.DataFrame(havaDurumu2)
print(havaDurumu)
print(havaDurumu2)
print("\n")
#simdi eksik verilerle alakali islem yapalim

# veri olmayan satirlarin hepsini datadan cikardi. (tek seferligine)
print(havaDurumu.dropna()) 
# veri olmayan sutunlarin hepsini atti (tek seferligine)
print(havaDurumu.dropna(axis=1)) 
# veri olmayan sutunlarin arasindan 2 den fazla deger olmayan sutunu datadan cikardi. (tek seferligine)
print(havaDurumu.dropna(axis=1, thresh=2)) 
# datada bosluk olan tum yerleri tek seferligine datadanb siler. tam tersi icin inplace = True
print(havaDurumu.fillna(10))
print("\n") 

# GroupBy dataframe.groupby(name)
sirketData = {"Departman" : ["Yazilim","Yazilim","Pazarlama","Pazarlama","Hukuk","Hukuk"],
          "Calisan Ismi" : ["Ahmet","Mehmet","Hamza","Samet","Emirhan","Hatice"],
          "Maas" : [1000,1500,2000,2500,3000,3500]
          }
sirketData = pd.DataFrame(sirketData)
print(sirketData)
sirketObje = sirketData.groupby("Departman")
print(sirketObje)# burada obje olarak output verecek
print("\n")
#obje ile baska fonksiyonlar kullanma
# bu obje ile olasilik istatistik dersinde yapabildigimiz her seyi yapıyoruz
print(sirketObje.describe()) # butun aciklamalari alma
print(sirketObje.min()) # minimum deger
print(sirketObje.max()) # max deger
# print(sirketObje.mean()) # ortalama alma
print(sirketObje.count()) # departmanda olan veri sayisi
print("\n")
# Concat
# Concat fonksiyonu ile farkli data frameleri birlestirme
spor = {"Isim" : ["Ahmet","Mehmet","Hamza","Samet"],
        "Spor" : ["Kosu","Yuzme","Kosu","Basketbol"],
        "Kalori" : [100,200,300,400]
        }
spor1 = {"Isim" : ["Emirhan","Hatice","Fatih","Furkan"],
         "Spor" : ["Futbol","Badminton","Voleybol","Basketbol"],
         "Kalori" : [500,600,700,800]
         }
spor = pd.DataFrame(spor)
spor1 = pd.DataFrame(spor1)
# concat isleminde axis belirtmezsek axis = 0 alinir sutun birlestireceksek column = 1 verilmelidir.
spor2 = pd.concat([spor,spor1],axis=0) # burada 2 den fazla data frame de verebiliriz ama burada iki tane verdik

#MERGE
mergeSpor = {"Isim" : ["Ahmet","Mehmet","Hamza","Samet"],
        "Spor" : ["Kosu","Yuzme","Kosu","Basketbol"]
        }
mergeSpor1 = {"Isim" : ["Ahmet","Mehmet","Hamza","Samet"],
        "Kalori" : [100,200,300,400]
        }
mergeSpor = pd.DataFrame(mergeSpor)
mergeSpor1 = pd.DataFrame(mergeSpor1)
# bir datada kalori degerleri yoktur ve isim degerleri ayni oldugu gorulmustur
# bu durumda merge yapilabilir merge yapildiktan sonra kalori degeri mergeSpor'a eklenmis olur
sporData = pd.merge(mergeSpor,mergeSpor1,on="Isim")
print(sporData)
print("\n")
#Farkli Operasyonlar
print(sirketData["Departman"].unique()) # kac farkli departman varsa hepsini gormemizi saglar
print(sirketData["Departman"].nunique()) # departman sayisini gosterir
print(sirketData["Departman"].value_counts()) # her bir departmanda kac kkisi oldugunu gosterir
print("\n")
def netMaas(maas):
        return maas * 0.66
print(sirketData["Maas"].apply(netMaas)) # bizim daha once yazdigimiz fonksiyonu dataya uygulayabilmemizi saglar
print(sirketData["Departman"].isnull()) # datada null degeri var mı diye kontrol eder
print("\n")

# Pivot Table
cartoon = {"Karakter Sinifi" : ["South Park","South Park","Simpson","Simpson","Simpson"],
           "Karakter Ismi" : ["Cartman","Kenny","Homer","Bart","Bart"],
           "Karakter Puani" : [10,11,12,20,25]}
cartoon = pd.DataFrame(cartoon)
print(cartoon)
# pivot_table yardimiyla tabloda ayni elemandan iki tane data var ise ikisine tek atama yapabiliyoruz farkli fonksiyon atamasi da yapabiliriz 
print(cartoon.pivot_table(values="Karakter Puani",index=["Karakter Sinifi","Karakter Ismi"],aggfunc=np.sum))
