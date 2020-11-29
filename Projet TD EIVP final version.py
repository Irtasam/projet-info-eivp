# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 10:05:47 2020

@author: acer
"""

#Projet info EIVP

import datetime
import matplotlib.pyplot as plt
import os

os.getcwd()
monfichier = open('EIVP_KM.csv','r')
L = []
for ligne in monfichier.readlines():
    L += ligne.split('\t')
L = L[6:]
L = [i for i in L]
#print(L)

#L : liste de ttes les données sans les entêtes

#passer d'une chaîne de liste à une liste de str
def str_list(chaine):
    L = []
    char = ""
    for c in chaine:
        if c != ";":
            char += c
        elif char != "":
            L.append(char)
            char = ""
    L.append(char)
    return L

lig = len(L)    #nombre de lignes
col = len(L[0]) #nombre de colonnes
#Transformer les lignes en listes de str pour récupérer les données
for i in range(lig):
    L[i] = str_list(L[i])
    
ID = []
Noise = []
Temp = []
Hum = []
Lum = []
CO2 = []
Sent_at = []

Donnees = [ID, Noise, Temp, Hum, Lum, CO2, Sent_at]

#Fonction pour passer d'une date en str à une date et heure en list
def datetimelist(chaine):
    Date = []
    nb = ''
    for c in chaine:
        if c in "0123456789":
            nb += c
        elif nb != '':
            Date.append(int(nb))
            nb = ''
    if nb != '':
        Date.append(int(nb))
    return Date
    
for i in range(lig):
    for j in range(col):
        donnee = L[i][j]
        if j != 6:
            donnee = float(donnee)  #passer de str à nombre si possible
        else:
            donnee = donnee[:-7]    #pour enlever "+0200\n"
            
            date = datetimelist(donnee)     #avoir la date et l'heure en liste
            donnee = datetime.datetime(date[0],date[1],date[2],date[3],date[4],date[5])
            #pour avoir la date en classe Datetime pour être correctement exploitée
        Donnees[j].append(donnee)  #insérer dans les bonnes listes les bonnes données

#Là on a les différentes listes ID, Noise, etc avec leurs données numériques
#Pour Sent_at, on a les dates et heures en datetime.datetime
        


#plt.figure()
#plt.plot(Sent_at,Temp)
#plt.title('Température en fct du temps')
#plt.xlabel('Temps')
#plt.ylabel('Température')
