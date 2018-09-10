n = int(input("Digite um numero para calcular o fatorial"))
contador = 1
acumulador = 1
while contador <= n:
    acumulador = acumulador * contador
    contador = contador + 1
    print ("Fatorial :", acumulador)