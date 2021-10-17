import jikanvision
import cv2

cap = cv2.VideoCapture(0)
faceMeshDetector = jikanvision.FaceMeshDetector()

while True:
    success, img = cap.read()
    meshes, img = faceMeshDetector.findFaces(img)

    cv2.imshow("Jikan Vision Library - FaceMeshDetector Module", img)
    cv2.waitKey(1)
