from random import *
lista=[]
for i in range(100):
    a=randrange(10, 100)
    lista.append(a)
for u in range(len(lista)):
    print(lista[i], end=" ")
    if ((u+1)%10==0):
        print("\n")