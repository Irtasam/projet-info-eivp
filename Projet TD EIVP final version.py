# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 10:05:47 2020

@author: acer
"""

#Projet info EIVP

import datetime
import matplotlib.pyplot as plt
import numpy as np
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
        
def niveau_sonore():
    minNoise = min(Noise)
    maxNoise = max(Noise)
    medianeNoise = np.median(Noise)
#    moyNoise = np.mean(Noise)
#    varNoise = np.var(Noise)
#    ecartypeNoise = varNoise**0.5
    
    print("Niveau sonore \n",)
    print("Minimum = "+str(minNoise))
    print("Maximum = "+str(maxNoise))
    print("Médiane = "+str(medianeNoise))
#    print("Moyenne = "+str(moyNoise))
#    print("Variance = "+str(varNoise))
#    print("Ecart-type = "+str(ecartypeNoise))
    
    plt.figure()
    plt.plot(Sent_at,Noise)
#    plt.plot(Sent_at, lig*[moyNoise + ecartypeNoise], c='orange', lw=2, label='µ + sigma')
#    plt.plot(Sent_at, lig*[moyNoise - ecartypeNoise], c='orange', lw=2, label='µ - sigma')
    plt.title('Niveau sonore en fonction du temps')
    plt.xlabel('Temps')
    plt.ylabel('Niveau sonore (dBA)')
#    plt.legend()
    plt.show()

def température():
    minTemp = min(Temp)
    maxTemp = max(Temp)
    medianeTemp = np.median(Temp)
    moyTemp = np.mean(Temp)
    varTemp = np.var(Temp)
    ecartypeTemp = varTemp**0.5
    
    print("Température \n",)
    print("Minimum = "+str(minTemp))
    print("Maximum = "+str(maxTemp))
    print("Médiane = "+str(medianeTemp))
    print("Moyenne = "+str(moyTemp))
    print("Variance = "+str(varTemp))
    print("Ecart-type = "+str(ecartypeTemp))
    
    plt.figure()
    plt.plot(Sent_at, Temp, c='blue')
    plt.plot(Sent_at, lig*[moyTemp + ecartypeTemp], c='orange', lw=2, label='µ + sigma')
    plt.plot(Sent_at, lig*[moyTemp - ecartypeTemp], c='orange', lw=2, label='µ - sigma')
    plt.title('Température en fonction du temps')
    plt.xlabel('Temps')
    plt.ylabel('Température (°C)')
    plt.legend()
    plt.show()
    
def humidité_relative():
    minHum = min(Hum)
    maxHum = max(Hum)
    medianeHum = np.median(Hum)
    moyHum = np.mean(Hum)
    varHum = np.var(Hum)
    ecartypeHum = varHum**0.5
    
    print("Humidité relative \n",)
    print("Minimum = "+str(minHum))
    print("Maximum = "+str(maxHum))
    print("Médiane = "+str(medianeHum))
    print("Moyenne = "+str(moyHum))
    print("Variance = "+str(varHum))
    print("Ecart-type = "+str(ecartypeHum))
    
    plt.figure()
    plt.plot(Sent_at, Hum)
    plt.plot(Sent_at, lig*[moyHum + ecartypeHum], c='orange', lw=2, label='µ + sigma')
    plt.plot(Sent_at, lig*[moyHum - ecartypeHum], c='orange', lw=2, label='µ - sigma')
    plt.title('Humidité relative en fonction du temps')
    plt.xlabel('Temps')
    plt.ylabel('Humidité relative (%)')
    plt.legend()
    plt.show()

def luminosité():
    minLum = min(Lum)
    maxLum = max(Lum)
    medianeLum = np.median(Lum)
    moyLum = np.mean(Lum)
    varLum = np.var(Lum)
    ecartypeLum = varLum**0.5
    
    print("Luminosité \n",)
    print("Minimum = "+str(minLum))
    print("Maximum = "+str(maxLum))
    print("Médiane = "+str(medianeLum))
    print("Moyenne = "+str(moyLum))
    print("Variance = "+str(varLum))
    print("Ecart-type = "+str(ecartypeLum))
    
    plt.figure()
    plt.plot(Sent_at, Lum)
    plt.plot(Sent_at, lig*[moyLum + ecartypeLum], c='orange', lw=2, label='µ + sigma')
    plt.plot(Sent_at, lig*[moyLum - ecartypeLum], c='orange', lw=2, label='µ - sigma')
    plt.title('Niveau lumineux en fonction du temps')
    plt.xlabel('Temps')
    plt.ylabel('Niveau lumineux (lux)')
    plt.legend()
    plt.show()
    
def co2():
    minCO2 = min(CO2)
    maxCO2 = max(CO2)
    medianeCO2 = np.median(CO2)
    moyCO2 = np.mean(CO2)
    varCO2 = np.var(CO2)
    ecartypeCO2 = varCO2**0.5
    
    print("Quantité de CO2 \n",)
    print("Minimum = "+str(minCO2))
    print("Maximum = "+str(maxCO2))
    print("Médiane = "+str(medianeCO2))
    print("Moyenne = "+str(moyCO2))
    print("Variance = "+str(varCO2))
    print("Ecart-type = "+str(ecartypeCO2))
    
    plt.figure()
    plt.plot(Sent_at, CO2)
    plt.plot(Sent_at, lig*[moyCO2 + ecartypeCO2], c='orange', lw=2, label='µ + sigma')
    plt.plot(Sent_at, lig*[moyCO2 - ecartypeCO2], c='orange', lw=2, label='µ - sigma')
    plt.title('Quantité de CO2 en fonction du temps')
    plt.xlabel('Temps')
    plt.ylabel('Quantité de CO2 (ppm)')
    plt.legend()
    plt.show()

