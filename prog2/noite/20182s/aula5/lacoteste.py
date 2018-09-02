import random
jogar = True
while jogar == True:
    print("Jogo de dados")
    num = int(input("Digite um numero entre 1 e 6"))
    aleatorio = random.randint(1, 6)
    print("Numero sorteado foi", aleatorio)
    if aleatorio==num:
        print("Voce ganhou")
    else:
        print("Você perdeu")

    resposta = input("Deseja continuar jogando ?(S/N)")
    if resposta == "N":
        jogar = False

print("Fim do Jogo")