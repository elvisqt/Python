mizael = higor = denis = macienio = nulos = 0

print("7 Mizael, 18 Higor, 72 Denis, 14 Macienio")
print("Digite 'fim' ou Enter vazio para encerrar.")

while True:
    voto = input("Vote: ")
    if voto == "" or voto == "fim":
        break
    try:
        voto = int(voto)
    except:
        print("Entrada inválida")
        continue

    if voto == 7:
        mizael += 1
    elif voto == 18:
        higor += 1
    elif voto == 72:
        denis += 1
    elif voto == 14:
        macienio += 1
    else:
        nulos += 1

print("\nResultados:")
print("Mizael", mizael)
print("Higor", higor)
print("Denis", denis)
print("Macienio", macienio)
print("Nulos", nulos)

todososvotos = max(mizael, higor, denis, macienio)
if todososvotos == 0:
    print("Sem votos válidos")
else:
    vencedores = []
    if mizael == todososvotos:
        vencedores.append("Mizael")
    if higor == todososvotos:
        vencedores.append("Higor")
    if denis == todososvotos:
        vencedores.append("Denis")
    if macienio == todososvotos:
        vencedores.append("Macienio")
    print("Vencedor(es):", ", ".join(vencedores))
