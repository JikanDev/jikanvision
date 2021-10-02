"""
Body Tracking Module
By : JikanDev
Website : https://jikandev.xyz/
"""
import cv2
import mediapipe as mp


class BodyDetector:
    """
    Finds Bodies using the mediapipe library. Exports the landmarks in pixel format.
    Also provides bounding box info of the body found.
    """

    def __init__(self, mode=False, model=1, smooth_lm=True, segmentation=False, smooth_segmentation=True,
                 minDetectCon=0.5, minTrackCon=0.5):
        """
        :param mode: In static mode, detection is done on each image: slower.
        :param model: Complexity of the pose landmark model: 0, 1 or 2. See
        details in https://solutions.mediapipe.dev/pose#model_complexity.
        :param smooth_lm: Whether to filter landmarks across different input
        images to reduce jitter.
        :param segmentation: Whether to predict segmentation mask.
        :param smooth_segmentation: Whether to filter segmentation across different input
        images to reduce jitter.
        :param minDetectCon: Minimum Detection Confidence Threshold.
        :param minTrackCon: Minimum Tracking Confidence Threshold.
        """
        self.mode = mode
        self.model = model
        self.smooth_lm = smooth_lm
        self.segmentation = segmentation
        self.smooth_segmentation = smooth_segmentation
        self.minDetectCon = minDetectCon
        self.minTrackCon = minTrackCon

        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.model, self.smooth_lm, self.segmentation, self.smooth_segmentation,
                                     self.minDetectCon, self.minTrackCon)
        self.mpDraw = mp.solutions.drawing_utils

        self.lmList = []

    def findBodies(self, img, draw=True, drawBboxs=False):
        """
        Finds bodies in a BGR image.
        :param img: Image to find the hands in.
        :param draw: Flag to draw the output on the image.
        :param drawBboxs: Flag to draw bboxs on the draw output.
        :return: Image with or without drawings.
        """
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)

        allBodies = []
        h, w, c = img.shape

        if self.results.pose_landmarks:
            bodyLms = self.results.pose_landmarks

            myBody = {}

            mylmList = []
            xList = []
            yList = []

            for id, lm in enumerate(bodyLms.landmark):
                px, py = int(lm.x * w), int(lm.y * h)
                mylmList.append([px, py])
                xList.append(px)
                yList.append(py)

            xmin, xmax = min(xList), max(xList)
            ymin, ymax = min(yList), max(yList)
            boxW, boxH = xmax - xmin, ymax - ymin
            bbox = xmin, ymin, boxW, boxH
            cx, cy = bbox[0] + (bbox[2] // 2), bbox[1] + (bbox[3] // 2)

            myBody["lmList"] = mylmList
            myBody["bbox"] = bbox
            myBody["center"] = (cx, cy)

            allBodies.append(myBody)

            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
                if drawBboxs:
                    cv2.rectangle(img, (bbox[0] - 20, bbox[1] - 100), (bbox[0] + bbox[2] + 20, bbox[1] + bbox[3] + 20), (255, 255, 255), 2)
                    cv2.putText(img, "Body", (bbox[0] - 30, bbox[1] - 110), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
        if draw:
            return allBodies, img
        else:
            return allBodies


def main():
    """
    Example code to use the module.
    """
    cap = cv2.VideoCapture(0)  # Get your camera
    detector = BodyDetector()  # Call the BodyDetector class

    while True:
        success, img = cap.read()  # If success, img = read your camera image
        bodies, img = detector.findBodies(img)  # bodies & img call the findBodies() function of BodyDetector

        if bodies:
            # Body 1
            body1 = bodies[0]
            lmList1 = body1["lmList"]  # List of 21 Landmark points
            bbox1 = body1["bbox"]  # Bounding box info x,y,w,h
            centerPoint1 = body1['center']  # Center of the body cx,cy

            if len(bodies) == 2:
                # Body 2
                body2 = bodies[1]
                lmList2 = body2["lmList"]  # List of 21 Landmark points
                bbox2 = body2["bbox"]  # Bounding box info x,y,w,h
                centerPoint2 = body2['center']  # Center of the body cx,cy

        cv2.imshow("Body Tracking Module", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()