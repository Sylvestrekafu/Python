# Somme des éléments d'une liste
liste2 =[x for x in range(10)]

print("----------------------")
print("La liste est :", liste2)
somme = 0

for i in liste2:
    somme+=i

print("La somme des élements de la liste est :", somme)
print("--------------------------------------------")
print("Somme :", sum(liste2))