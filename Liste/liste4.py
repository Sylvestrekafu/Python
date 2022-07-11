liste1= [i for i in range(10)] # Liste des éléments allant de 0 à 9
liste2 = [i**2 for i in range(10)] # Liste du carré des éléments de 0 à 9
liste3 = [2*x+3 for x in range(10)] # Liste des éléments prennant la valeur de la fonction affine 2x +3 de chanque élémént de 0 à 9

liste4 = [ i for i in range(10) if i%2==0] # Liste contenant les valeurs paires entre 0 à 9

liste5 =[ i for i in range(10) if i%2==1] # Liste contenant les valeurs impairs entre 0 à 9
liste6 =[ i for i in range(20) if i%3==0] # Liste des multiples de 3 entre 0 et 19



# Afficher les listes
print("liste1 :", liste1)
print("---------------------------------------")
print("liste2 :", liste2)
print("---------------------------------------")
print("liste3 :", liste3)
print("---------------------------------------")
print("liste4 :", liste4)
print("---------------------------------------")
print("liste5 :", liste5)
print("---------------------------------------")
print("liste6 :", liste6)