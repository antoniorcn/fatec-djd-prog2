notas = [10.0, 8.0, 0.0, 4.0, 9.0, 0.0, 1.0]
# media = (notas[0] + notas[1] + notas[2] + notas[3] + notas[4]) / 5
soma = 0
contador = 0
while contador <= len(notas) - 1:
    soma = soma + notas[contador]
    contador = contador + 1
media = soma / len(notas)
print("Media : ", media)