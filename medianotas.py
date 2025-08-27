nome = input("Diga qual seu nome: ")
nota1 = int(input("Nota 1: "))
nota2 = int(input("Nota 2: "))
nota3 = int(input("Nota 3: "))

media = (nota1+nota2+nota3)/3

if media >= 7:

    print("Parabens",nome ,"você esta na media, sua media foi" , media)

else:
    print(nome,"você foi reprovado, sua media foi", media)