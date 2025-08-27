a = int(input("Valor: "))
s = input("op: ")
b = int(input("Valor: "))

def op(s):
    if s == "+":
        resultado = a + b
    elif s == "-":
        resultado = a - b
    elif s == "*":
        resultado = a * b
    elif s == "/":
        resultado = a / b
    return resultado

print(op(s))