import random
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
lista2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
MISNUMEROS=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
print(random.sample(lista, 14))
l1 = [1, 2, 3, 4, 5]
l2 = [9, 8, 7, 6, 5]



MARCA=0
for x in range(0,50000):
   CARTON=random.sample(lista, 14)
   print(CARTON)
   if(set(CARTON) == set(MISNUMEROS) and MARCA!=1):
    MARCA=1

print("MARCA:",MARCA)