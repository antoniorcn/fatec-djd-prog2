temp = int(input("digite a temp"))
frio = temp < 18
hora = int(input("digite a hora"))
tarde = hora > 20

vir_faculdade = not (frio and tarde)

print ("Vir para a faculdade : ", vir_faculdade)
