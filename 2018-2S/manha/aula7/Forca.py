import random

lista   = ['COXINHA', 'RISOLI', 'ESFIHA', 'PIZZA']
tam = len(lista)
n = random.randint(0, tam - 1)
palavra = lista[n]
print (palavra)

acertos = []
for i in range(0, len(palavra)):
    acertos.append('_')

while True:
    for i in range(0, len(palavra)):
        print( acertos[i], " ", end="")

    letra = input("Digite uma letra:")

    for i in range(0, len(palavra)):
        if palavra[i] == letra:
            acertos[i] = letra

