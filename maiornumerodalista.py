numeros = [1,4,6,8,12,16,19,25,55,66,35,78,99,205,306,400,354,289]
maior = numeros[0]
for numero in numeros:
    if numero > maior:
        maior = numero
        print(numero)
