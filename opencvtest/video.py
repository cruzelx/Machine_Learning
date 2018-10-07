import cv2,matplotlib.pyplot as plt

cap=cv2.VideoCapture('testvid.wmv')
print(cap.isOpened())

while (cap.isOpened()):
	ret,frame=cap.read()
	cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
#	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	cv2.imshow('frame',frame)
	#ret=cap.set(4,320)
	
	if cv2.waitKey(1) & 0xFF==ord('q'):
		break


cap.release()
cv2.destroyAllWindows()
