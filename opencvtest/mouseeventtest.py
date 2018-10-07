import cv2,numpy as np
def draw_art(event,x,y,flags,param):
	if event==cv2.EVENT_LBUTTONDBLCLK:
		cv2.circle(img,(x,y),100,(255,255,255),5)
	elif event==cv2.EVENT_RBUTTONDOWN:
		cv2.rectangle(img,(x-50,y-50),(x+50,y+50),(200,200,0),5)

img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('mouseevent')
cv2.setMouseCallback('mouseevent',draw_art)

while(True):
	cv2.imshow('mouseevent',img)
	if cv2.waitKey(20) & 0xff==ord('q'):
		break

cv2.destroyAllWindows()
