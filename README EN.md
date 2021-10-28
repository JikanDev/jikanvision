# Jikan Vision

![Lib Version](https://img.shields.io/pypi/v/jikanvision.svg)
![Python Versions](https://img.shields.io/pypi/pyversions/jikanvision.svg)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/d56be9b7e37a4913881d6f154f780332)](https://www.codacy.com/gh/JikanDev/jikanvision/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=JikanDev/jikanvision&amp;utm_campaign=Badge_Grade)

Jikan Vision is a python library based on Mediapipe and OpenCV. The goal of this library is to simplify and accelerate the creation of python projects based on Mediapipe.

## Supported features :
## _Detection of one or more hands:_
- The follow-up of one or more hands.
- Display of 20 points on each hand (s).
- Retrieval of the coordinates of the 20 points per hand (s) in lists.
- Display of the type of hand (Right or Left).
- Recovery of the type of hand.
- Display of a "box" around each hand (s).
- Retrieval of the coordinates of this "box".
- Recovery of the center of this "box".

## _Detection of a body:_
- Tracking a body.
- Display of 32 points on the body.
- Retrieve the 32 points in a list.
- Display of a "box" around the body.
- Retrieval of the coordinates of the "box".
- Recovery of the center of this "box".

## _Detection of one or more faces:_
- Detection of one or more faces.
- Display of a square around the face (s) and the detection score.

## _Mesh on or more faces:_
- Detection of one or more faces then application of a mesh of 468 points.
- Display of the mesh and contours of the face.
- Retrieval of the coordinates of the 468 points in a list.

## First installation
Simply do this command to install Jikan Vision and all this dependencies :

```sh
pip install jikanvision
```

or

```sh
py -m pip install jikanvision
```

## Update the library

Simply do this command to update Jikan Vision and all this dependencies :

```sh
pip install -U jikanvision
```

or

```sh
py -m pip install -U jikanvision
```

## Dependencies
- [Mediapipe](https://pypi.org/project/mediapipe/) - MediaPipe offers cross-platform, customizable ML solutions for live and streaming media.
- [OPenCV-Python](https://pypi.org/project/opencv-python/) - Pre-built CPU-only OpenCV packages for Python.

## Tested on the following Python versions:

- 3.9
- 3.8
- 3.7
- 3.6
- 3.5
