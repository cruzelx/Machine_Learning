import cv2,numpy as np
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
def funt(x):
	print(x)
cv2.createTrackbar('Red \t','image',0,255,funt)
cv2.createTrackbar('Blue \t','image',0,255,funt)
cv2.createTrackbar('Green \t','image',0,255,funt)
cv2.createTrackbar('OFF \n ON','image',0,1,funt)
font=cv2.FONT_HERSHEY_DUPLEX
while(1):
	cv2.imshow('image',img)
	if cv2.waitKey(1) & 0xff==ord('q'):
		break
	r=cv2.getTrackbarPos('Red \t','image')
	b=cv2.getTrackbarPos('Blue \t','image')
	g=cv2.getTrackbarPos('Green \t','image')
	s=cv2.getTrackbarPos('OFF \n ON','image')
	
	if s==0:
		img[:]=0
	else:
		img[:]=[b,g,r]
		cv2.putText(img,'(R={}, B={}, G={})'.format(r,b,g),(75,200),font,1,(255,100,200),1,cv2.LINE_AA)

cv2.destroyAllWindows()
