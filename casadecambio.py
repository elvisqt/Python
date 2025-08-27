carteira = float(input("Valor que tenho na carteira: "))
dia = float(input("Cotação atual: "))

def saldo(carteira, dia):
    conv = dia / carteira
    return conv

att = saldo(carteira, dia)
print(att)
