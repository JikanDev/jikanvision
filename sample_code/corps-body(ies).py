import jikanvision
import cv2

cap = cv2.VideoCapture(0)
bodyDetector = jikanvision.BodyDetector()

while True:
    success, img = cap.read()
    bodies, img = handDetector.findBodies(img)

    cv2.imshow("Jikan Vision Library - BodyDetector Module", img)
    cv2.waitKey(1)
