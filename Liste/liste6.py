mylist = [1, 2, 3, 4, 5]

#le premier élément
print("Premier éléménts",mylist[0])  # 1

#troisième élément
print("Troisième éléments",mylist[2])  # 3

# cinquième élément
print(mylist[4])  # 5


# Ajouter une valeur à la liste
mylist.append(6)
mylist.append("a")
print("------------------")
print(mylist)

#Suppression d'éléments
mylist.remove(1) # supprimer l'élémént 1 de la liste
mylist.pop(1)
print("------------------")
print(mylist)
print("------------------")
mylist.pop(1)