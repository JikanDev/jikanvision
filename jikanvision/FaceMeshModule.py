"""
Face Mesh Module
By : JikanDev
Website : https://jikandev.xyz/
"""
import cv2
import mediapipe as mp


class FaceMeshDetector():
    """
    Find 468 Landmarks using the mediapipe library. Exports the landmarks in pixel format.
    """

    def __init__(self, mode=False, maxFaces=1, refine_lm=False, minDetectCon=0.5, minTrackCon=0.5):
        """
        :param mode: In static mode, detection is done on each image: slower.
        :param maxFaces: Maximum number of faces to detect.
        :param refine_lm: Whether to further refine the landmark coordinates
        around the eyes and lips, and output additional landmarks around the
        irises.
        :param minDetectCon: Minimum Detection Confidence Threshold.
        :param minTrackCon: Minimum Tracking Confidence Threshold.
        """
        self.mode = mode
        self.maxFaces = maxFaces
        self.refine_lm = refine_lm
        self.minDetectCon = minDetectCon
        self.minTrackCon = minTrackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpDrawingStyles = mp.solutions.drawing_styles
        self.faceMesh = mp.solutions.face_mesh

        self.meshDetection = self.faceMesh.FaceMesh(mode, maxFaces, refine_lm, minDetectCon, minTrackCon)

    def findFaces(self, img, draw=True, drawTesselation=True):
        """
        Find faces in an image and return the bbox info
        :param img: Image to find the faces in.
        :param draw: Flag to draw the output contours of the mesh on the image.
        :param drawTesselation: Flag to draw the output tesselation of the mesh on the image.
        :return: Image with or without drawings.
        """
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.meshDetection.process(imgRGB)

        allFaces = []
        h, w, c = img.shape

        if self.results.multi_face_landmarks:
            for faceLms in self.results.multi_face_landmarks:
                myMesh = {}
                mylmList = []

                for id, lm in enumerate(faceLms.landmark):
                    px, py = int(lm.x * w), int(lm.y * h)
                    mylmList.append([px, py])

                myMesh["lmList"] = mylmList

                if draw:
                    self.mpDraw.draw_landmarks(img, faceLms, self.faceMesh.FACEMESH_CONTOURS, None)

                if drawTesselation:
                    self.mpDraw.draw_landmarks(img, faceLms, self.faceMesh.FACEMESH_TESSELATION, None,
                                               self.mpDrawingStyles.get_default_face_mesh_tesselation_style())

                allFaces.append(myMesh)

        return allFaces, img


def main():
    """
    Example code to use the module.
    """
    cap = cv2.VideoCapture(0)  # Get your camera
    detector = FaceMeshDetector()  # Call the FaceMeshDetector class

    while True:
        success, img = cap.read()  # If success, img = read your camera image
        meshes, img = detector.findFaces(img)  # meshes & img call the findFaces() function of FaceMeshDetector

        if meshes:
            # Mesh 1
            mesh1 = meshes[0]
            lmList1 = mesh1["lmList"]  # List of 21 Landmark points

            if len(meshes) == 2:
                # Mesh 2
                mesh2 = meshes[1]
                lmList2 = mesh2["lmList"]  # List of 21 Landmark points

        cv2.imshow("Face Mesh Module", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()