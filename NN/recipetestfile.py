import numpy as np, pandas as pd
from sklearn import svm

csvfile=input('enter csv file path: ')
data=pd.read_csv(csvfile)
df=pd.DataFrame(data)
print('available ingredients: ',list(df)[1:])
a,b=input('enter any two ingredients: ').split()
sugar_butter=df[[a,b]].as_matrix()
labels=np.where(df['Type']=='Muffin',0,1)
clf=svm.SVC(C=100)
clf.fit(sugar_butter,labels)

def f(x,y):
	l= clf.predict([[x,y]])
	if(l==0): print('Muffin.')
	else: print('either Cupcake or Scone.')

f(int(input('enter 1st ingredient ')),int(input('enter 2nd ingredient')))



