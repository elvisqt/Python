valor = int(input("Valor que deseja: "))

tabuada = valor
for i in range(1, 11):
    resultado = tabuada * i
    print(f"{tabuada} x {i} = {resultado}")