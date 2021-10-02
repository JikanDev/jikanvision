"""
Hand Tracking Module
By : JikanDev
Website : https://jikandev.xyz/
"""
import cv2
import mediapipe as mp


class HandDetector:
    """
    Finds Hands using the mediapipe library. Exports the landmarks in pixel format.
    Also provides bounding box info of the hand found.
    """

    def __init__(self, mode=False, maxHands=2, minDetectCon=0.5, minTrackCon=0.5):
        """
        :param mode: In static mode, detection is done on each image: slower.
        :param maxHands: Maximum number of hands to detect.
        :param minDetectCon: Minimum Detection Confidence Threshold.
        :param minTrackCon: Minimum Tracking Confidence Threshold.
        """
        self.mode = mode
        self.maxHands = maxHands
        self.minDetectCon = minDetectCon
        self.minTrackCon = minTrackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.minDetectCon, self.minTrackCon)
        self.mpDraw = mp.solutions.drawing_utils

        self.lmList = []

    def findHands(self, img, draw=True, drawBboxs=True, camFlip=True):
        """
        Finds hands in a BGR image.
        :param img: Image to find the hands in.
        :param draw: Flag to draw the output on the image.
        :param drawBboxs: Flag to draw bboxs on the draw output.
        :param camFlip: Flag to know if your camera flip your image.
        :return: Image with or without drawings.
        """
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        allHands = []
        h, w, c = img.shape

        if self.results.multi_hand_landmarks:
            for handType, handLms in zip(self.results.multi_handedness, self.results.multi_hand_landmarks):
                myHand = {}

                mylmList = []
                xList = []
                yList = []

                for id, lm in enumerate(handLms.landmark):
                    px, py = int(lm.x * w), int(lm.y * h)
                    mylmList.append([px, py])
                    xList.append(px)
                    yList.append(py)

                xmin, xmax = min(xList), max(xList)
                ymin, ymax = min(yList), max(yList)
                boxW, boxH = xmax - xmin, ymax - ymin
                bbox = xmin, ymin, boxW, boxH
                cx, cy = bbox[0] + (bbox[2] // 2), bbox[1] + (bbox[3] // 2)

                myHand["lmList"] = mylmList
                myHand["bbox"] = bbox
                myHand["center"] = (cx, cy)

                if camFlip:
                    if handType.classification[0].label == "Right":
                        myHand["type"] = "Left"
                    else:
                        myHand["type"] = "Right"
                else:
                    myHand["type"] = handType.classification[0].label
                allHands.append(myHand)

                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
                    if drawBboxs:
                        cv2.rectangle(img, (bbox[0] - 20, bbox[1] - 20), (bbox[0] + bbox[2] + 20, bbox[1] + bbox[3] + 20), (255, 255, 255), 2)
                        cv2.putText(img, myHand["type"], (bbox[0] - 30, bbox[1] - 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
        if draw:
            return allHands, img
        else:
            return allHands


def main():
    """
    Example code to use the module.
    """
    cap = cv2.VideoCapture(0)  # Get your camera
    detector = HandDetector()  # Call the HandDetector class

    while True:
        success, img = cap.read()  # If success, img = read your camera image
        hands, img = detector.findHands(img)  # hands & img call the findHands() function of HandDetector

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

        cv2.imshow("Hands Tracking Module", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()