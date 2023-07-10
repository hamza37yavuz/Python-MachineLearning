from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

# ilkleme
classifier = Sequential()

# Adım 1 - Convolution
# input shape'in 64,64,3 olmasının sebebi: burada 3 3 farklı ürün olduğu için bu şekilde yazılır.
# 64 okuduğumuz resimlerden 64 e 64 piksellik resimler elde etmek istememizdir
classifier.add(Convolution2D(32, 3, 3, input_shape = (64, 64, 3), activation = 'relu'))

# Adım 2 - Pooling
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# 2. convolution katmanı
classifier.add(Convolution2D(32, 3, 3, activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Adım 3 - Flattening
classifier.add(Flatten())

# Adım 4 - YSA
# classifier.add(Dense(units=6,kernel_initializer='glorot_uniform',activation='relu'))
classifier.add(Dense(units=128, activation = 'relu'))
# Cikis katmaninin sigmoid olmasi tavsiye edilir
classifier.add(Dense(units=1, activation = 'sigmoid'))

# CNN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# CNN ve resimler
# Image data generator dizinde bulunan resimleri sirasiyla ram e yukler.
# RAM dostu bir calisma saglar. 
from keras.preprocessing.image import ImageDataGenerator

# Burada resim isleme ile ilgili bazi filtrelemeler yapilmistir
train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

training_set = train_datagen.flow_from_directory('veriler/training_set',
                                                 target_size = (64, 64),
                                                 batch_size = 1,
                                                 class_mode = 'binary')

test_set = test_datagen.flow_from_directory('veriler/test_set',
                                            target_size = (64, 64),
                                            batch_size = 1,
                                            class_mode = 'binary')
# Burada yapay sinir agi train ediliyor.
# classifier.fit_generator(verbose=1,)
classifier.fit_generator(training_set,
                         steps_per_epoch = 8000,
                         validation_data = test_set,
                         epochs=5
                         )
# classifier.fit_generator(training_set,
#                          steps_per_epoch = 8000,
#                          nb_epoch = 1,
#                          validation_data = test_set,
#                          nb_val_samples = 2000)


import numpy as np
import pandas as pd


test_set.reset()
# Burada verbose 1 yaparsak ok seklinde akmayi gorecegiz
pred=classifier.predict_generator(test_set,verbose=1)
#pred = list(map(round,pred))
pred[pred > .5] = 1
pred[pred <= .5] = 0

print('prediction gecti')
#labels = (training_set.class_indices)

# Confusion matrix icin asagidaki islemi yapiyoruz
test_labels = []

for i in range(0,int(203)):
    # test_set[i][1] burada gercekteki 1 mi 0 mı oldugu ile ilgili degeri aliyoruz
    # test_set[i][1] bize bir label dondurur.
    test_labels.extend(np.array(test_set[i][1])) 
    
print('test_labels')
print(test_labels)

#labels = (training_set.class_indices)
'''
idx = []  
for i in test_set:
    ixx = (test_set.batch_index - 1) * test_set.batch_size
    ixx = test_set.filenames[ixx : ixx + test_set.batch_size]
    idx.append(ixx)
    print(i)
    print(idx)
'''
dosyaisimleri = test_set.filenames
#abc = test_set.
#print(idx)
#test_labels = test_set.
sonuc = pd.DataFrame()
sonuc['dosyaisimleri']= dosyaisimleri
sonuc['tahminler'] = pred
sonuc['test'] = test_labels   

from sklearn.metrics import confusion_matrix


cm = confusion_matrix(test_labels, pred)
print (cm)



