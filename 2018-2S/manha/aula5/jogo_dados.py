import random
r = "S"
print("Jogo de dados")
vida = 3
while r == "S":
    n = int(input("Escolha um numero entre 1 e 6"))
    a = random.randint(1, 6)
    if n == a:
        print("Ganhou")
        continue
    else:
        print("Perdeu", END="")
        vida = vida - 1
        if vida <= 0:
            break
    r = input("Deseja jogar de novo (S/N) ?")
else:
    print("Parabéns você desistiu enquanto ainda tinha vidas")
print("Fim do programa")
