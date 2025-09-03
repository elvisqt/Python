import random

lista = []
for i in range(10):
    numero = random.randint(1, 100)
    lista.append(numero)
numerolista = len(lista)
for numero in range(numerolista):
    for ordna in range(0, numerolista - numero - 1):
        if lista[ordna] > lista[ordna + 1]:
            lista[ordna] > lista[ordna + 1], lista[ordna] > lista[ordna + 1]
            print(lista)
