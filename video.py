import cv2

face_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + "haarecascade_frontalface_default.xml")

img = cv2.imread('face.jpg')

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Result', img)

cv2.waitKey(0)

#cap = cv2.VideoCapture(0)

#while True:

#    success, frame = cap.read()
 #   cv2.imshow('camera', frame)

  #  if cv2.waitKey(1) & 0xff == ord('q'):
   #     break
