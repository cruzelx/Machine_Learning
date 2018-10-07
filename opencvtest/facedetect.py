import numpy as np, cv2,sys,math

cap=cv2.VideoCapture(0)
casPath=sys.argv[1]
fCascade=cv2.CascadeClassifier(casPath)
while(True):
	ret,frame=cap.read()
	if ret==True:
		gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		faces=fCascade.detectMultiScale(
			gray,
			scaleFactor=1.5,
			minNeighbors=5,
			minSize=(25,25)
		)
		for (x,y,w,h) in faces:
			print(x,y,w,h)
			cv2.rectangle(frame,(x,y),(x+h,y+h),(100,160,220),3)
			cv2.rectangle(frame,(x,y),(x+110,y-30),(100,160,220),-1)
#			cv2.circle(frame,(int(x+w/2),int(y+h/2)),int(math.sqrt((int(w/2))**2+(int(h/2))**2)),(20,20,160),3)
			font=cv2.FONT_HERSHEY_DUPLEX
			cv2.putText(frame,'Face',(int(x+4),int(y)),1,font,(155,255,255),2,cv2.LINE_AA)
		cv2.imshow('faceDetect',frame)
		if cv2.waitKey(1) &0xff==ord('q'):
			break
	else:
		break

cap.release()
cv2.destroyAllWindows()
