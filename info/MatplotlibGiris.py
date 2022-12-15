# -*- coding: utf-8 -*-
"""
Spyder kullanildi
"""
# MATPLOTLIB
import numpy as np
import matplotlib.pyplot as plt

# GRAFIK OLUSTURMA
yas = [10,22,30,40,50,60,65,70,75,80]
kilo = [30,70,80,85,90,92,95,100,90,85]
# numpy dizisine donusturelim
yas = np.array(yas)
kilo = np.array(kilo)
# Simdi grafige bakalim
plt.plot(yas,kilo,"r")
# Grafikte diger islemler
plt.xlabel("Yas")
plt.xlabel("Kilo")
plt.title("Yasa Gore Kilo Degisimi")
# diger ornek
x = np.arange(0, 5, 0.1)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)

# OZELLESTİRME

numpyDizisi1 = np.linspace(0,10,20)
numpyDizisi2 = numpyDizisi1**3
"""
plt.plot(dizi1,dizi2,"g--")
#simdi ayni ekranda iki tane grafik gorelim
plt.subplot(1,2,1) # 1 satir 2 grafikten 1. grafik
plt.plot(dizi1,dizi2,"g--") # bu grafik bir onceki satirda verildigi yere gelir
plt.subplot(1,2,2)
plt.plot(dizi1,dizi2,"g*-")
# figure
myFigure = plt.figure() # instance aldik
# burada 0.2 sol taraftaki eksenin baslangic noktasi, 0.2 alt taraftaki eksenin baslangic noktasi
figureAxess = myFigure.add_axes([0.4,0.4,0.6,0.6]) # son iki indis with ve height degerleridir
figureAxess.plot(dizi1,dizi2,"g") # dizi baslangici
#Diger islemler
figureAxess.set_xlable("X Ekseni Veri Ismi")
figureAxess.set_ylable("Y Ekseni Veri Ismi")
figureAxess.set_title("Grafik Basligi")
"""

#OZELLESTIRME 2
"""
figure2 = plt.figure()
# alt satirda yer alan birinci 0.1 degeri grafiğin x eksenindeki konumunu
# ikinci 0.1 grafiğin y eksenindeki konumunu belirler.
eksen1 = figure2.add_axes([0.1,0.1,0.7,0.7])
eksen2 = figure2.add_axes([0.3,0.3,0.3,0.3])

eksen1.plot(dizi1,dizi2,"b")
eksen1.set_xlable("X Ekseni")
eksen1.set_ylable("Y Ekseni")
eksen1.set_title("Ana Grafik Basligi")

eksen2.plot(dizi2,dizi1,"b")
eksen2.set_xlable("Kucuk X Ekseni")
eksen2.set_ylable("Kucuk Y Ekseni")
eksen2.set_title("Kucuk Grafik Basligi")
"""
# OZELLESTIRME 3
"""
# eger subplots'un içine deger yazmasaydim eksen tuple olacakti
(myFigure, eksenler) = plt.subplots(1,2)
print(type(eksenler)) # artik bu bir array
for eksen in eksenler:
    eksen.plot(dizi1,dizi2,"g")
    eksen.set_xlable("X Ekseni")
plt.tight_layout()
"""
# AYRINTILAR VE DOSYAYI KAYDETME
"""
newFigure = plt.figure()
# bir üst satirda dpi değeri verilebilir
grafik = newFigure.add_axes([0.1,0.1,0.9,0.9])
grafik.plot(dizi1,dizi1**2,label = "Dizinin karesi")
grafik.plot(dizi1,dizi2,label = "Dizinin küpü")
grafik.legend(loc = 6)
newFigure.savefig("figure.png",dpi = 200) # piksel kalitesiile ilgili deger 
"""
# ILERI SEVİYE
# renk kullanimi
(yeniFigur, yeniEksen) = plt.subplots()
yeniEksen.plot(numpyDizisi1, numpyDizisi1 + 2, color="blue", linewidth = 1.0)
yeniEksen.plot(numpyDizisi1, numpyDizisi1 + 3, color ="yellow", linewidth = 1.0)

yeniEksen.plot(numpyDizisi1, numpyDizisi1 + 4, color = "#C96F23", linestyle = "-.")
yeniEksen.plot(numpyDizisi1, numpyDizisi1 + 5, color = "#C96F23", linestyle = ":")
yeniEksen.plot(numpyDizisi1, numpyDizisi1 + 6, color = "#C96F23", linestyle = "--")

yeniEksen.plot(numpyDizisi1, numpyDizisi1 + 7, color = "#000000", linestyle = "--", marker = "o",markersize = 8, markerfacecolor="red")
yeniEksen.plot(numpyDizisi1, numpyDizisi1 + 8, color = "#000000", linestyle = "-")

# SCATTER
plt.scatter(numpyDizisi1,numpyDizisi2)

# HISTOGRAM
newArray = np.random.randint(0,100,50)
plt.hist(newArray)

# BOXPLOT
plt.boxplot(newArray)

# Matplotlib websitesinden tutoriallarin ustunden gecebiliriz
