import numpy as np
"""
print("\n") outputta 1 satir bosluk birakmak icin konulmustur
"""
#normal liste olusturma
myList = [20,30,40]
#----numpy kullanimlari----
print(np.array(myList))

#matris listesi
matrisList = [[10,20,30],[20,30,40],[30,40,50]]
print(np.array(matrisList))
print("\n")

#range-arange
print(np.arange(0,10))
print(np.arange(0,10,2))

#zeros (Goruntu islemede kullanilabilir)
print(np.zeros(5))
print(np.zeros((3,3)))

#ones
print("\n")
print(np.ones(5))
print(np.ones((3,3)))

#linspace evenLinspace
print("\n") 
print(np.linspace(0,20,10)) # 0-20 (0-20 dahil) arasinda 10 tane birbirine esit uzaklikta sayi bulur

# eye verdiginiz degere göre birim matris olusturur
print("\n")
print(np.eye(3)) #birim matris: bir matrisle carpildiginda etkisi olmayan matris

# random
print("\n")
print(np.random.randn(4)) # dizi dondurme
print(np.random.randn(3,3)) # matris dodurme
print(np.random.randint(1,10)) # 1 ile 10 arasinda bir random deger
print(np.random.randint(1,100,5)) # 1 ile 100 arasinda 5 elemanli dizi
dizi1 = np.random.randint(1,100,10)
print(dizi1)

#numpy dizi metotlari
print("\n")
dizi2 = np.arange(0,30)
print(dizi2)
print(dizi2.reshape(5,6)) # matrise cevirdi
print("\n")
print(dizi1.max()) #dizideki maximum elemani bulur
print(dizi1.min()) #dizideki minimum elemani bulur
print(dizi1.argmax()) #dizideki maximum degerin indeksini bulur
print(dizi1.argmin()) #dizideki minimum degerin indeksini bulur
print(dizi1.shape) #dizinin eleman sayisini veriyor

#numpyOperasyonlar
print("\n")
print(dizi1[1])
print(dizi2[3:5])

dizi1[2:5] = -7 # diziden verilen indekslerin arasindaki degerleri verilen degerlerle degistirilir
print(dizi1)

dizi1[:] = 50
print(dizi1)

bolunmusDizi = dizi1[3:7] # bunu daha once yapmistik
print(bolunmusDizi)

bolunmusDizi[:] = 20 # bu degisiklik yapildigi zaman dizi1'de de degisim olmustur
print(bolunmusDizi)
print("\n")
print(dizi1)# bu degisim olmamasi icin dizi once kopyalanmali sonra kopya alan dizi uzerinden islemler yapilmasi lazim

dizi1kopya = dizi1.copy() # bu sekilde yapildiktan sonra yukaridaki islemler yapilirsa ana dizi1'de degisim olmaz.

#Matris
print("\n")
list1 = [[1,2,3],[4,5,6],[7,8,9]]
matris1 = np.array(list1)
print(matris1)
print("\n")
print(matris1[1])
print(matris1[1][1])
print(matris1[1,1])
print(matris1[2:,])
print(matris1[:,1]) #ortadaki sutun
print(matris1[:,1:2]) #ortadaki sutun yukardan asagı
print(matris1[2:,2:]) #3. sutun 3. satir

list2 = [[1,2,3,10],[4,5,6,11],[7,8,9,12],[13,14,13,15]]
matris2 = np.array(list2)
print("\n")
print(matris2)
print("\n")
print(matris2[[0,3,2]]) #1. satir 3. satir ve 2. satiri almamizi sagladi

#numpy dizi operasyonlar
print("\n")
dizi3 = np.random.randint(1,100,20)
print(dizi3)
sonDizi = dizi3 > 20
print("\n")
print(sonDizi)
print("\n")
print(dizi3[sonDizi])
print("\n")
print(dizi3[dizi3>20])
print("\n")
print("işlemler")
print(dizi3+dizi3)
print(dizi3*dizi3)
print(dizi3/dizi3) 
print(dizi3-dizi3) 
print(np.sqrt(dizi2)) # karekok al
