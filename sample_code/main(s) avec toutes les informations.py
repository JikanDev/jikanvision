import jikanvision
import cv2

cap = cv2.VideoCapture(0)  # Trouver votre caméra
handDetector = jikanvision.HandDetector()  # Appeller la classe HandDetector

while True:
    success, img = cap.read()  # En cas de succès, img = lire l'image de caméra
    hands, img = handDetector.findHands(img)  # hands & img appellent la fonction findHands() de HandDetector

    if hands:
        # Main 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # Liste des 21 points de repère
        bbox1 = hand1["bbox"]  # Informations sur la boîte x,y,w,h
        centerPoint1 = hand1['center']  # Centre de la main cx,cy
        handType1 = hand1["type"]  # Type de main "Gauche" ou "Droite"

        if len(hands) == 2:
            # Main 2
            hand2 = hands[1]
            lmList2 = hand2["lmList"]  # Liste des 21 points de repère
            bbox2 = hand2["bbox"]  # Informations sur la boîte x,y,w,h
            centerPoint2 = hand2['center']  # Centre de la main cx,cy
            handType2 = hand2["type"]  # Type de main "Gauche" ou "Droite"

    cv2.imshow("Jikan Vision Library - HandDetector Module", img)
    cv2.waitKey(1)
