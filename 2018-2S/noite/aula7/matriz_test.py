# Para criar uma lista com 5 elementos '_'
# ex. ['_', '_', '_', '_', '_']
print("Lista com elementos iguais")
lista = []
for i in range(5):
    lista.append('_')
print("Lista: ", lista)

# Alternativa
lista_alternativa = ['_' for i in range(5)]
print("Modo Alternativdo de criar lista: ", lista_alternativa)


# Para criar uma lista com 6 numeros
# ex. [0, 1, 2, 3, 4, 5]
print("Lista com numeros na sequencia")
lista = []
for i in range(6):
    lista.append(i)
print("Lista: ", lista)

# Alternativa
lista_alternativa = [i for i in range(6)]
print("Modo Alternativdo de criar lista: ", lista_alternativa)


# Para criar uma lista com 6 numeros pares
# ex. [0, 2, 4, 6, 8, 10]
print("Lista com 6 numeros pares na sequencia")
lista = []
for i in range(6):
    lista.append(i * 2)
print("Lista: ", lista)

# Alternativa
lista_alternativa = [i * 2 for i in range(6)]
print("Modo Alternativdo de criar lista: ", lista_alternativa)



# Para criar uma matriz com elementos repetidos
# ex.   [   ['_', '_', '_'],
#           ['_', '_', '_'],
#           ['_', '_', '_']
#       ]
print("Matriz 3x3 com elementos repetidos")
matriz = []
for l in range(3):
    linha = []
    for c in range(6):
        linha.append('_')
    matriz.append(linha)
print("Matriz: ", matriz)

# Alternativa
matriz_alternativa = [['_' for c in range(3)] for l in range(3)]
print("Modo Alternativdo de criar matriz: ", matriz_alternativa)