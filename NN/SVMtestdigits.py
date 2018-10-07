##SVM
import matplotlib,matplotlib.pyplot as plt, numpy as np
from sklearn import datasets,svm
digits=datasets.load_digits()
clf=svm.SVC(gamma=0.00001,C=100)
x,y=digits.data[:-1],digits.target[:-1]
clf.fit(x,y)
print('prediction: ',clf.predict(digits.data[-0].reshape(1,-1)))
plt.imshow(digits.images[-0],cmap=plt.cm.gray_r,interpolation="nearest")
plt.show()
