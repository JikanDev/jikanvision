import jikanvision
import cv2

cap = cv2.VideoCapture(0)
faceDetector = jikanvision.FaceDetector()

while True:
    success, img = cap.read()
    img, bboxs = faceDetector.findFaces(img)

    cv2.imshow("Jikan Vision Library - FaceDetector Module", img)
    cv2.waitKey(1)
