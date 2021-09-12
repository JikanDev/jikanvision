import jikanvision
import cv2

cap = cv2.VideoCapture(0)  # Get your camera
handDetector = jikanvision.HandDetector()  # Call the HandDetector class

while True:
    success, img = cap.read()  # If success, img = read your camera image
    hands, img = handDetector.findHands(img)  # hands & img call the findHands() function of HandDetector

    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmark points
        bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
        centerPoint1 = hand1['center']  # Center of the hand cx,cy
        handType1 = hand1["type"]  # Hand Type "Left" or "Right"

        if len(hands) == 2:
            # Hand 2
            hand2 = hands[1]
            lmList2 = hand2["lmList"]  # List of 21 Landmark points
            bbox2 = hand2["bbox"]  # Bounding box info x,y,w,h
            centerPoint2 = hand2['center']  # Center of the hand cx,cy
            handType2 = hand2["type"]  # Hand Type "Left" or "Right"

    cv2.imshow("Jikan Vision Library - HandDetector Module", img)
    cv2.waitKey(1)
