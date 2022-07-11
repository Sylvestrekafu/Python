liste3 =[] # création d'une liste vide
print('liste vide :',liste3) # afficher la liste

print("--------------------------------")
"""Ajouter des éléments dans la liste"""
liste3.append(1)
liste3.append("a")

print("éléments de la liste :",liste3) # afficher les éléménts de la liste

# Créer une liste longue

liste = [i for i in range(1,10)] # création une liste d'éléménts allant de 1 à 9
co=liste.copy() # création d'une nouvelle liste par copie 
co1 = liste[:]
print(co)
print(co1)
print("**********************************")
print(liste) # Afficher les élémént de la liste
print(liste[0])
print(type(liste))
# Créer une liste avec numpy
import  numpy as np
listnumpy =np.arange(1,10)
print("------------------------")
print(listnumpy)
print(listnumpy[0]) # Afficher le premier éléménts
print(type(listnumpy))

