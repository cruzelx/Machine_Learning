import numpy as np
import os
import random
import cv2

categories = ["applefruit", "banana", "mango", "orange", "papaya", "pineapple"]
path = '/home/iamlex/Desktop/Neural_Network/datasets'
training_set = []
count = 0
for category in categories:
    for img in os.listdir(os.path.join(path, category)):
        try:
            images = cv2.imread(os.path.join(path, category, img))
            #images = cv2.resize(images, (40, 40))
            training_set.append([images, categories.index(category)])
            count = count+1
            print(count, category,images.shape)
        except Exception as e:
            print(str(e))


random.shuffle(training_set)
X = []
y = []

for features, labels in training_set:
    X.append(features)
    y.append(labels)

print(np.array(X).shape)

np.save('/home/iamlex/Desktop/Neural_Network/features1',
        np.array(X).reshape(-1, 40, 40, 3))
np.save('/home/iamlex/Desktop/Neural_Network/labels1', np.array(y))
