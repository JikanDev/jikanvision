"""
Face Detection Module
By : JikanDev
Website : https://jikandev.xyz/
"""
import cv2
import mediapipe as mp


class FaceDetector():
    """
    Find faces in realtime using the light weight model provided in the mediapipe library.
    """
    def __init__(self, minDetectCon=0.5, model=0):
        """
        :param minDetectCon: Minimum Detection Confidence Threshold.
        :param model: Model adaptation, 0 to select a short-range model that works
        best for faces within 2 meters from the camera, and 1 for a full-range
        model best for faces within 5 meters.
        """
        self.minDetectCon = minDetectCon
        self.model = model

        self.mpFaceDetection = mp.solutions.face_detection
        self.mpDraw = mp.solutions.drawing_utils
        self.faceDetection = self.mpFaceDetection.FaceDetection(self.minDetectCon, self.model)

    def findFaces(self, img, draw=True):
        """
        Find faces in an image and return the bbox info
        :param img: Image to find the faces in.
        :param draw: Flag to draw the output on the image.
        :return: Image with or without drawings.
                 Bounding Box list.
        """
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceDetection.process(imgRGB)

        bboxs = []
        if self.results.detections:
            for id, detection in enumerate(self.results.detections):
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, ic = img.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
                bboxs.append([id, bbox, detection.score])
                if draw:
                    img = self.fancyDraw(img,bbox)

                    cv2.putText(img, f'{int(detection.score[0] * 100)}%', (bbox[0], bbox[1] - 20), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)

        return img, bboxs

    def fancyDraw(self, img, bbox, l=30, t=5, rt= 1):
        x, y, w, h = bbox
        x1, y1 = x + w, y + h

        cv2.rectangle(img, bbox, (255, 255, 255), rt)

        cv2.line(img, (x, y), (x + l, y), (0, 0, 255), t)
        cv2.line(img, (x, y), (x, y+l), (0, 0, 255), t)

        cv2.line(img, (x1, y), (x1 - l, y), (0, 0, 255), t)
        cv2.line(img, (x1, y), (x1, y+l), (0, 0, 255), t)

        cv2.line(img, (x, y1), (x + l, y1), (0, 0, 255), t)
        cv2.line(img, (x, y1), (x, y1 - l), (0, 0, 255), t)

        cv2.line(img, (x1, y1), (x1 - l, y1), (0, 0, 255), t)
        cv2.line(img, (x1, y1), (x1, y1 - l), (0, 0, 255), t)
        return img


def main():
    """
    Example code to use the module.
    """
    cap = cv2.VideoCapture(0)  # Get your camera
    detector = FaceDetector()  # Call the FaceDetector class

    while True:
        success, img = cap.read()  # If success, img = read your camera image
        img, bboxs = detector.findFaces(img)  # img & bboxs call the findFaces() function of FaceDetector

        cv2.imshow("Face Detection Module", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()