import jikanvision
import cv2

cap = cv2.VideoCapture(0)
handDetector = jikanvision.HandDetector(maxHands=2)

while True:
    success, img = cap.read()
    img = handDetector.findHands(img)

    cv2.imshow("Jikan Vision Library - HandDetector Module", img)
    cv2.waitKey(1)
