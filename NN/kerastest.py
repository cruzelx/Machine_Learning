import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense
white = pd.read_csv('winequality-white.csv', sep=';')
red = pd.read_csv('winequality-red.csv', sep=';')
'''
fig,ax=plt.subplots(1,2)
ax[0].scatter(red['quality'],red['sulphates'],facecolor='green',alpha=0.7,label='RED WINE')
ax[1].scatter(white.quality,white['sulphates'],facecolor='blue',alpha=0.7,label='WHITE WINE')
fig.subplots_adjust(left=0.2,right=0.8,bottom=0.1,top=0.8,hspace=0.05,wspace=0.8)
ax[0].set_ylim([0,2.5])
ax[0].set_xlim([0,10])
ax[1].set_ylim([0,2.5])
ax[1].set_xlim([0,10])
ax[0].set_title('Red Wine')
ax[1].set_title('White Wine')
ax[0].set_xlabel('Quality')
ax[0].set_ylabel('Sulphates')
ax[0].legend()
ax[1].set_xlabel('Quality')
ax[1].set_ylabel('Sulphates')
ax[1].legend()
'''
###########
white['type'] = 1
red['type'] = 0
wines = red.append(white, ignore_index=True)
'''
import seaborn as sns
corr=wines.corr()
sns.heatmap(corr,xticklabels=corr.columns.values,yticklabels=corr.columns.values)
plt.show()
'''
###########
'''
fig.suptitle('Quality vs Sulphates')
plt.show()
'''
# print(wines.columns)
X = wines.ix[:, 0:11]
# print(X)
y = np.ravel(wines.type)
# print(y)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42)

scaler = StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

model = Sequential()
model.add(Dense(12, activation='relu', input_shape=(11,)))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
'''
print(model.output_shape)
print(model.summary())
print(model.get_config())
print(model.get_weights())
'''
model.compile(loss="binary_crossentropy",
              optimizer="adam", metrics=['accuracy'])
model.fit(X_train, y_train, epochs=5, batch_size=1, verbose=1)
print(model.predict(X_test)[:5])
print(y_test[:5])
