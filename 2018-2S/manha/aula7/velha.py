velha = [ ['_' for i in range(3)] for j in range(3)]
peca = 'X'
while True:
	for i in range(3):
		linha = velha[i]
		for j in range(3):
			print(linha[j], end=" ")
		print("")
		
	lin = int(input("Informe a linha"))
	col = int(input("Informe a coluna"))

	velha[lin][col] = peca