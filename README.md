# projet-info-eivp
(à cause de problèmes quand a la maitrise des logiciel git et de différents problèmes, nous avons pris des noes à part et les mettont maintenant)
(voici le travail accompli par le binôme sans dissociation des tâches)


essaie 1

apprendre l'utilisation de git en classe

***Partie 1: Début du projet en groupe

apprehension du sujet
apprendre comment ajouter un fichier csv dans python
création de l'algorithme
ajout du fichier csv dans l'algorithme 
création des fonctions de base


problèmes rencontrés:
-complications et disfonctinnement de l'ouverture du fichier csv
-incompréhension de l'utilisation de git


***Partie 2: Première pistes et premier échecs

continuation du projet

tentative de création d'un algorithme transformant le fichier csv en listes

correction du problème d'ouverture du fichier csv dans python

problème à gérer les premieres valeurs du fichier sont des noms nécéssaire de les supprimer
création d'un algorithme supprimant la première valeur des listes crées avec la fonction remove
--> échec de fontionnement 

pour résoudre cela création d'un algorithme permettant de retirer les 7 premières cases du fichier csv avant de séparer ses colonnes en listes

optimisation de l'algorithme 

***Partie 3: Phase final du projet

initiation partiel de l'utilisation de git plus explicative avec le professeur responsable, resultats mitigé
-->porblème pour utiliser le commit et push qui refuse de sauvegarder l'avancé sur git sur le fichier de github

début de l'écriture du rendu à partir des notes

explications et aide à l'initiation de git grâce à des camarades

optimisation de l'algorithme --> succès quant à l'affichage des données grâce à une autre bibliothèque : os.
Optimmisation du classement des données dans des listes avec une méthode consistant à parcourir les données qu'une seule fois.
Problème : comment gérer les dates. Solution : bibliothèque pandas. Problème : python ne reconnaît pas sent_at comme une liste.
Contourner ceci en convertissant les dates en str au format datetime.datetime

Désormais : possible de tracer des courbes avec matplotlib.pyplot en prenant la liste des dates simplement comme abscisse et une colonne de données comme ordonnée.

Programme finalisé : possibilité d'afficher les courbes après avoir affiché les données statistiques dans la console, et ce pour chacune des grandeurs mesurées.
