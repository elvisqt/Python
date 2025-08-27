nome = input("Nome: ")
peso = float(input("Peso: "))
altura = float(input("Altura: "))
imc = peso / (altura ** 2)

print(f"{nome} seu IMC é {imc:.2f}")
if imc < 18.5:
    print("Magreza")
elif 18.5 <= imc < 24.9:
    print("Peso normal")
elif 24.9 <= imc < 29.9:
    print("Sobrepeso")
elif 30 <= imc < 34.9:
    print("Obesidade Grau 1")
elif 35 <= imc < 39.9:
    print("Obesidade Grau 2")
else:
    print("Obesidade Grau 3")
