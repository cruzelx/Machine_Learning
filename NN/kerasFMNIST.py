from keras.datasets import fashion_mnist
from keras.utils import normalize
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout,Flatten,Convolution2D,MaxPooling2D
import matplotlib.pyplot as plt
import numpy as np
import cv2
(X_train,y_train),(X_test,y_test)=fashion_mnist.load_data()
X_train = normalize(X_train)
X_test = normalize(X_test)
X_train=X_train.reshape(X_train.shape[0],28,28,1)
X_test=X_test.reshape(X_test.shape[0],28,28,1)

print(X_train.shape,y_train.shape)
#model 
print(np.unique(y_test))
model=Sequential()
model.add(Convolution2D(32,3,3,activation='relu',input_shape=(28,28,1)))
model.add(Convolution2D(32,3,3,activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2),strides=2))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128,activation='relu'))
model.add(Dropout(0.25))
model.add(Dense(10,activation='softmax'))

model.compile(loss='sparse_categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(X_train,y_train,epochs=10,verbose=1)
print(model.evaluate(X_test,y_test))

model.save('fmnistmodel.h5')
fashionModel=load_model('fmnistmodel.h5')
img=cv2.imread('Trouser.png',0)
gray=cv2.resize(img,(28,28))
#gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
prediction=fashionModel.predict(gray.reshape(-1,28,28))
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

print(class_names[np.argmax(prediction)])
plt.imshow(gray)
plt.show()  
