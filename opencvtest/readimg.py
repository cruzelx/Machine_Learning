import numpy as np, cv2, matplotlib.pyplot as plt

img=cv2.imread('screen.png',0)
print(img)
#cv2.namedWindow('image',cv2.WINDOW_NORMAL)
plt.imshow(img,interpolation='spline16')
plt.xticks([])
plt.yticks([])
plt.show()


