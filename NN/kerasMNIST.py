from keras.datasets import mnist 
from keras.layers import Dense,Activation,Flatten,Dropout
from keras.models import Sequential,load_model
from keras.utils import normalize
import matplotlib.pyplot as plt
import tensorflow as tf

mnist=tf.keras.datasets.mnist
(X_train, y_train),(X_test, y_test)=mnist.load_data()

X_train=normalize(X_train)
X_test=normalize(X_test)
print(X_train.shape)

model=Sequential()
model.add(Flatten())
model.add(Dense(128,activation='relu',input_shape=(28,28)))
model.add(Dense(128,activation='relu'))
model.add(Dense(10,activation='softmax'))

model.compile(loss='sparse_categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(X_train,y_train,batch_size=64,epochs=5,verbose=1)

model.save('numReader.h5')
eMmodel=load_model('numReader.h5')
prediction=eMmodel.predict([X_test])

import numpy as np
print(np.argmax(prediction[3]))
print(prediction[3])
plt.imshow(X_test[3])
plt.show()