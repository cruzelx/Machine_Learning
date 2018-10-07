import numpy as np
import cv2
import os
import random
import matplotlib.pyplot as plt

path = '/home/iamlex/Desktop/Neural_Network/catdogimgdataset/PetImages'
categories = ['Dog', 'Cat']
training_data = []
i = 0
for category in categories:
    for img in os.listdir(os.path.join(path, category)):

        try:
            imgs = cv2.imread(os.path.join(path, category, img), 0)
            imgs = cv2.resize(imgs, (100, 100))
            training_data.append([imgs, categories.index(category)])
            i = i+1
            print(i)

        except Exception as e:
            pass

random.shuffle(training_data)

X = []
y = []

for features, labels in training_data:
    X.append(features), y.append(labels)


np.save('/home/iamlex/Desktop/Neural_Network/features',
        np.array(X).reshape(-1, 100, 100, 1))
np.save('/home/iamlex/Desktop/Neural_Network/labels',
        np.array(y))
