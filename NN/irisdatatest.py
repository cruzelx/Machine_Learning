import matplotlib,matplotlib.pyplot as plt, numpy as np
from sklearn import datasets,svm

iris=datasets.load_iris()
clf=svm.SVC(gamma=0.0001,C=100)
x,y=iris.data[:-1],iris.target[:-1]
print(len(x),len(y))

clf.fit(x,y)
print('prediction: ',clf.predict(np.array([5,3,0.1,0.22]).reshape(1,-1)))
#plt.imshow(iris.images[1,2,3,4],cmap=plt.cm.gray_r, interpolation="nearest")
#plt.show()
