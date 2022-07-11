#Manipuler les listes
liste1 = [i for i in  range(10)]
liste1.index(5)

print(liste1)
print("-----------------------------------")
print(liste1.index(4))
print("-----------------------------------")
print("Nombre de la valeur 2 est :",liste1.count(2))
print("-----------------------------------")
liste1.reverse()

print("Ordre croisssant :", liste1)

print("-----------------------------------")
liste1.sort() # Mettre les éléments de la liste dans l'ordre croissant

print("Ordre décroissant : ", liste1)
print("-----------------------------------")
print("Longueur de la liste:", len(liste1))