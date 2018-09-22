velha = []
for i in range(3):
    linha = []
    for l in range(3):
        linha.append('_')
    velha.append(linha)

peca = 'X'
while True:
    for lin in range(3):
        for col in range(3):
            print(velha[lin][col], end=" ")
        print()

    lin = int(input("Digite a linha"))
    col = int(input("Digite a coluna"))

    velha[lin][col] = peca

    if peca == 'X':
        peca = 'O'
    else:
        peca = 'X'