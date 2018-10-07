import matplotlib,matplotlib.pyplot as plt, numpy as np, pandas as pd
import seaborn as sns
from sklearn import svm
from sklearn import datasets

data = pd.read_csv('recipedataset.csv')
sns.lmplot('Sugar','Butter',data=data,hue='Type',palette='Set1',fit_reg=False,scatter_kws={"s":70})
print(data.head())
sugar_butter=data[['Sugar','Butter']].as_matrix()
sugar=data[['Sugar']].as_matrix()
butter=data[['Butter']].as_matrix()
type_label=np.where(data['Type']=='Muffin',0,1)
clf=svm.SVC(C=100,kernel='linear')
clf.fit(sugar_butter,type_label)
print(clf.support_vectors_)
print(type_label)
#plt.scatter(sugar,butter)
plt.show()
print(sugar_butter)
