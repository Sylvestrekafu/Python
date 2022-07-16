"""
Calcul de la somme des éléments d'une liste avec différentes méthodes
"""
a =range(10)
liste1 = list(a)
print(liste1)
print("*--------------------------------")
print(*liste1) # Afficher les élémnts de la liste
print("--------------------------------")
print("somme:",sum(liste1))
somme =0
for x in liste1:
    somme+=x


print("somme:", somme)

s =sum([x for x in liste1])
print("somme:", s)