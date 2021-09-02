import jikanvision
import cv2

cap = cv2.VideoCapture(0)
faceDetector = jikanvision.FaceDetector()
handDetector = jikanvision.HandDetector(maxHands=2)

while True:
    success, img = cap.read()
    img = handDetector.findHands(img)
    img, bboxs = faceDetector.findFaces(img)

    cv2.imshow("Jikan Vision Librarye", img)
    cv2.waitKey(1)
