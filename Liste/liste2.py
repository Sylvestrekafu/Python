import  numpy as np
liste2 = np.arange(0,20, 2, dtype =int)
liste3 =[ x**2 for x in liste2  if x%2==0]
nb = 0
print(liste2)
print("-----------------------------")
print(liste3)
