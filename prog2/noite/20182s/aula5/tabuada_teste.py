print("Programa que imprime a tabuada")
numero = 5
while numero <= 255:
    print("\n\n\n")
    for n in range(1, 11):
        resultado = numero * n
        print(numero, "X", n, "=", resultado)
    numero = numero + 1

print("Fim do programa")