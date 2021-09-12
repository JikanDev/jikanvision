# Jikan Vision
## _FR_

Voici des exemples de petits codes pour pouvoir rapidement comprendre la librairie :

_Détécter un/des visage(s)_

```sh
import jikanvision
import cv2

cap = cv2.VideoCapture(0)
faceDetector = jikanvision.FaceDetector()

while True:
    success, img = cap.read()
    img, bboxs = faceDetector.findFaces(img)

    cv2.imshow("Jikan Vision Library - FaceDetector Module", img)
    cv2.waitKey(1)
```

_Détécter une/des main(s)_
```sh
import jikanvision
import cv2

cap = cv2.VideoCapture(0)
handDetector = jikanvision.HandDetector()

while True:
    success, img = cap.read()
    hands, img = handDetector.findHands(img)

    cv2.imshow("Jikan Vision Library - HandDetector Module", img)
    cv2.waitKey(1)
```

_Détécter un/des visage(s) Et une/des main(s)_
```sh
import jikanvision
import cv2

cap = cv2.VideoCapture(0)
faceDetector = jikanvision.FaceDetector()
handDetector = jikanvision.HandDetector()

while True:
    success, img = cap.read()
    hands, img = handDetector.findHands(img)
    img, bboxs = faceDetector.findFaces(img)

    cv2.imshow("Jikan Vision Librarye", img)
    cv2.waitKey(1)
```
##
##
## _EN_

Here are examples of small codes to quickly understand the library:

_Detect a face (s)_
```sh
import jikanvision
import cv2

cap = cv2.VideoCapture(0)
faceDetector = jikanvision.FaceDetector()

while True:
    success, img = cap.read()
    img, bboxs = faceDetector.findFaces(img)

    cv2.imshow("Jikan Vision Library - FaceDetector Module", img)
    cv2.waitKey(1)
```

_Detect a hand (s)_
```sh
import jikanvision
import cv2

cap = cv2.VideoCapture(0)
handDetector = jikanvision.HandDetector()

while True:
    success, img = cap.read()
    hands, img = handDetector.findHands(img)

    cv2.imshow("Jikan Vision Library - HandDetector Module", img)
    cv2.waitKey(1)
```

_Detect a face (s) AND a hand (s)_
```sh
import jikanvision
import cv2

cap = cv2.VideoCapture(0)
faceDetector = jikanvision.FaceDetector()
handDetector = jikanvision.HandDetector()

while True:
    success, img = cap.read()
    hands, img = handDetector.findHands(img)
    img, bboxs = faceDetector.findFaces(img)

    cv2.imshow("Jikan Vision Librarye", img)
    cv2.waitKey(1)
```

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
