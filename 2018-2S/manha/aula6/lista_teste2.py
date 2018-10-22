lista = [1, 2, 3]
print("Conteudo da lista :", lista)
outra_lista = [4, 5, 6, 7, 8, 9, 10, 5, 11, 12, 13, 5]
lista.extend(outra_lista)
#texto = "FATEC"
#lista.extend(texto)
print("Conteudo da lista :", lista)
elemento = lista.pop(2)
print("Conteudo da lista :", lista)
pos = lista.index(5, 10)
quantos = lista.count(5)
print("Numero 5 encontrado na posicao :", pos)
print("Numero 5 encontrado :", quantos, "vezes")
lista.reverse()
print("Conteudo da lista :", lista)