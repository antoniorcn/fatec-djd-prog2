def analisa_tempo(temperatura):
    if (temperatura > 10) and (temperatura < 30):
        descricao = "suave"
    elif (temperatura > 30):
        descricao = "quente"
    else:
        descricao = "frio"
    return temperatura, descricao

# r = analisa_tempo(20)
# print(r)
