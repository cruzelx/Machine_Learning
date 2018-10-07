import cv2,urllib.request,numpy as np

while True:
	imgr=urllib.request.urlopen('http://192.168.0.103:8080/shot.jpg')
	imgnp=np.array(bytearray(imgr.read()),np.uint8)
	img=cv2.imdecode(imgnp,-1)
	cv2.imshow('cam',img)
	if cv2.waitKey(10) &0xff==ord('q'):
		exit(0)
