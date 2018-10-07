##SVM
import matplotlib,matplotlib.pyplot as plt, numpy as np
from sklearn import datasets,svm
x=np.array([[0,0],[0,1],[1,0],[1,1]])
y=np.array([1,1,0,1])
clf=svm.SVC(C=100,decision_function_shape='ovo')
clf.fit(x,y)
print(clf.predict([[1,1]]))
plt.plot(x[:][0],x[:][1],x[:][2],x[:][3])
plt.show()
