provas = int(input("São quantas provas: "))
s = 0
nts = []
for i in range(provas):
    
    n = float(input("Nota aplicada: "))
    s += n
    nts.append(n)
media = s / provas

print ("Foram {} provas, notas {} dividido por 2 sua media sera {:.2f}".format(provas,nts,media))

if media >= 7:
    print("Você foi aprovado sua media foi {:.2f}".format(media))

elif media >= 5:
    print("Você ira precisar fazer recuperação sua media foi {:.2f} ".format(media))

else:
    print("Você não esta na media reprovado sua media foi {:.2f}".format(media))