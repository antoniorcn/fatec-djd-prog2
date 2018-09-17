
link = { 	"arma" :  "espada", "defesa" : "escudo",
"acessorios" : ["botina", "armadura", "chapeu"],
"vidas" : 10, "stamina":100 }

link["cavalo"] = "epona"

print (link.keys())
print (link.values())

if "cavalo" in link:
    print ("Link tem um cavalo chamado", link["cavalo"])
else:
    print("Link nao tem cavalo")
