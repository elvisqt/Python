nome = input("Qual seu nome: ")
idade = int(input("Qual sua idade: "))

idadecomeco = 14
idadefinal = 17




if idade >= idadecomeco and idade <= idadefinal:
    print("{} Você esta na idade certa para nosso evento sua idade é  {}".format(nome, idade))
elif idade <= idadecomeco:
    print("{} Você não tem entre {} a {} sua idade é a baixo de {}".format(nome,idadecomeco,idadefinal,idadecomeco))
elif idade >= idadefinal:
    print("{} Você não tem entre {} a {} sua idade é maior que {}".format(nome,idadecomeco,idadefinal,idadefinal))