import jikanvision
import cv2

cap = cv2.VideoCapture(0)
faceDetector = jikanvision.FaceDetector()
handDetector = jikanvision.HandDetector()

while True:
    success, img = cap.read()
    hands, img = handDetector.findHands(img)
    img, bboxs = faceDetector.findFaces(img)

    cv2.imshow("Jikan Vision Library", img)
    cv2.waitKey(1)
