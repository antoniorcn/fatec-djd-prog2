def cabecalho():
    print("#" * 80)
    print("Aula de Programação II")
    print("Aluno : Antonio Neto")
    print("RA : 123456")
    print("Exercicio: Exercício da Tabuada")
    print("#" * 80)


def fatorial(n=4):
    fat = 1
    for i in range(1, n+1):
        fat = fat * i
    print(fat)
    return n, fat


def analisatempo(temperatura):
    if (temperatura > 10) and (temperatura < 30):
        descricao = "padrão"
    elif (temperatura > 30):
        descricao = "quente"
    else:
        descricao = "frio"
    return temperatura, descricao


def faz_algo( numero1, numero2=20, texto="sem texto"):
    """
    Esta função calcula a soma do primeiro numero com o resto da divisão
    do segundo numero por 2
    :param numero1:
    :param numero2:
    :param texto:
    :return:
    """
    print(texto, numero1, " + ", numero2, "%2=", numero1 + (numero2 % 2))
    return numero1, numero2


def lista_parametros(**p):
    for chave in p.keys():
        print("Chave : ", chave, "  Valor : ", p[chave])