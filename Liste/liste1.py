liste1 =[0,1,2,3,4,5,6,7,8,9]
nb=0
# Trier les nombres pairs
Pair = [ x for x in liste1 if x%2==0]
Impair = [ x for x in liste1 if x%2==1 ]
counts = {item:liste1.count(item) for item in liste1}
#print(counts.get(2)

inverse = sorted(liste1, reverse=True)
inverse1 =liste1[::-1]
print(nb)
print(inverse)
print(inverse1)
print("#####################################")
print("Nombres pairs de la liste sont:", Pair)
print("**************************************************")
print("Noùbres impairs de la liste sont :", Impair)
pair=[]
impair =[]
for i in liste1:


    if i%2==0:
        nb+=1


        pair.append(i)

    else:
        impair.append(i)


print("-----------------------------")
print("Pairs: ", pair)
print("-------------------------")
print("impairs", impair)
pair1 =[]
for i in range(0, len(liste1)):
    if i%2==0:
        pair1.append(i)


print("-----------------------")
print("pair:",pair1 )
print("-----------------")
print(nb)