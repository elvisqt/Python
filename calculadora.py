import operator

n1 = input("Número: ")
soma = input("Operador (+, -, *, /): ")
n2 = input("Número: ")
try:
    n1 = float(n1)
    n2 = float(n2)
except ValueError:
    print("Errado você digitou letras")
    exit()
calculadora = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}
if soma not in calculadora:
    print("Errado você colocou operador inválido.")
elif soma == '/' and n2 == 0:
    print("Erro divisão por zero.")
else:
    resultado = calculadora[soma](n1, n2)
    print(f"{n1} {soma} {n2} = {resultado}")
