# Jikan Vision

![Lib Version](https://img.shields.io/pypi/v/jikanvision.svg)
![Python Versions](https://img.shields.io/pypi/pyversions/jikanvision.svg)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/d56be9b7e37a4913881d6f154f780332)](https://www.codacy.com/gh/JikanDev/jikanvision/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=JikanDev/jikanvision&amp;utm_campaign=Badge_Grade)

## _FR_

Jikan Vision est une librairie python basée sur Mediapipe et OpenCV. Le but de cette librairie est de simplifier et d'accélérer la création de projets python basés sur Mediapipe.

## Fonctionnalités prises en charge :
## _Détection de une ou plusieurs mains :_
- Le suivi d'une ou de plusieurs mains.
- Affichage de 20 points sur chaque main(s).
- Récupération des coordonnées des 20 points par main(s) dans des listes.
- Affichage du type de main (Droite ou Gauche).
- Récupération du type de main.
- Affichage d'une "boîte" autour de chaque main(s).
- Récupération des coordonnées de cette "boîte".
- Récupération du centre de cette "boîte".

## _Détection d'un corps :_
- Le suivi d'un corps.
- Affichage de 32 points sur le corps.
- Récupération des 32 points dans une liste.
- Affichage d'une "boîte" autour du corps.
- Récupération des coordonnées de la "boîte".
- Récupération du centre de cette "boîte".

## _Détection de un ou plusieurs visages :_
- La détection de un ou plusieurs visages.
- Affichage d'un carré autour du/des visage(s) et du score de détection.

## _Mesh sûr un/des visage(s) :_
- Détection d'un ou des visages puis application d'un mesh de 468 points.
- Affichage du mesh et des contours du visage.
- Récupération des coordonnées des 468 points dans une liste.

## Première installation

Faites simplement cette commande pour installer Jikan Vision et toutes ses dépendances :

```sh
pip install jikanvision
```
ou

```sh
py -m pip install jikanvision
```

## Mettre à jour la librairie

Faites simplement cette commande pour mettre à jour Jikan Vision et toutes ses dépendances :

```sh
pip install -U jikanvision
```

ou

```sh
py -m pip install -U jikanvision
```

## Dépendances

- [Mediapipe](https://pypi.org/project/mediapipe/) - MediaPipe propose des solutions de ML personnalisables et multiplateformes pour les médias en direct et en streaming.
- [OPenCV-Python](https://pypi.org/project/opencv-python/) - Packages OpenCV pré-construits uniquement pour le processeur pour Python.

## Testé sur les versions Python suivantes :

- 3.9
- 3.8
- 3.7
- 3.6
- 3.5

##
##
## License

Apache License 2.0

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
