import numpy as np,matplotlib.pyplot as plt,cv2
from keras.models import Sequential
from keras.layers import Flatten, Dropout, Conv2D,MaxPool2D,Dense
from keras.utils import normalize
from sklearn.model_selection import train_test_split
X=np.load('/home/iamlex/Desktop/Neural_Network/features1.npy')
y=np.load('/home/iamlex/Desktop/Neural_Network/labels1.npy')
X=X/255
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.10,random_state=42)
print(X_train.dtype)

print(X_train.shape)


model=Sequential()
model.add(Conv2D(64,3,3,activation='relu',input_shape=(30,30,1)))
model.add(MaxPool2D(pool_size=(2,2)))
#model.add(Dropout(0.25))
model.add(Conv2D(64,3,3,activation='relu'))
model.add(MaxPool2D(pool_size=(2,2)))
#model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128,activation='relu'))
model.add(Dense(6,activation='softmax'))

model.compile(loss='sparse_categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(X_train,y_train,epochs=20,verbose=1)

print(model.evaluate(X_test,y_test))
prediction=model.predict([X_test])

