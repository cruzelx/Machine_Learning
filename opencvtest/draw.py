import numpy as np,matplotlib.pyplot as plt, cv2

img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
img10=cv2.line(img,(0,10),(450,511),(200,160,110),10)
img1=cv2.rectangle(img,(50,100),(500,500),(0,255,0),12)
img2=cv2.circle(img,(255,255),150,(100,150,140),10)
img3=cv2.ellipse(img,(255,255),(100,70),0,360,180,255,-1)
pts=np.array([[100,200],[200,24],[400,30],[60,30]],np.int32)
pts=pts.reshape((-1,1,2))
img4=cv2.polylines(img,[pts],True,(0,255,255),12)
font=cv2.FONT_HERSHEY_DUPLEX
cv2.putText(img,'AlexBoy',(150,150),font,4,(0,255,0),4,cv2.LINE_AA)
cv2.imshow('image',img)
cv2.imshow('image',img1)
cv2.imshow('image',img2)
cv2.imshow('image',img3)
cv2.imshow('image',img4)

if(cv2.waitKey(0) & 0xff==ord('q')):
	cv2.destroyAllWindows()
