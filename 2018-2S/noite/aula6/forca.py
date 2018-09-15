import random

lista_palavras = ['FAATEC', 'ALUNA', 'PASTELARIA', 'JOGO', 'JOYSTYCK']
n = random.randint(0, len(lista_palavras) - 1)
palavra = lista_palavras[n]
vidas = 5
lst_palavra = list(palavra);
print("A palavra tem ", len(lst_palavra), " letras")

lst_acertos = ['_' for _ in lst_palavra]
while vidas > 0:
    print("Voce tem ", vidas, " vidas")
    for letra in lst_acertos:
        print(letra, " ", end="")
    l = input("\nDigite uma letra").upper()[0]
    contador_acertos = 0
    for i in range(len(lst_palavra)):
        if lst_palavra[i] == l:
            contador_acertos = contador_acertos + 1
            lst_acertos[i] = l
    print("Existem", contador_acertos, "ocorrencias nesta palavra")
    if contador_acertos == 0:
        vidas = vidas - 1

