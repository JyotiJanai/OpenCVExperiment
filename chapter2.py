import cv2
print("Package imported")

img = cv2.imread("Resources/Tiger1.jpg")
cv2.imshow("Output",img)
cv2.waitKey(1)

# cap =cv2.VideoCapture("Resources/TigerVid4.mp4")
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

while True:
	success, img = cap.read()
	cv2.imshow("Video",img)
	if cv2.waitKey(1)& 0xFF == ord('q'):
		break
