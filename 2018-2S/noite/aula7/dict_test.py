trevor = {"arma":"soco", "defesa":"punho",
          "hp":100, "vidas":1, "vivo":True,
          "itens" : ["granada", "faca", "soco inlges"]}

trevor["hp"] = trevor["hp"] + 5

if trevor["vivo"]:
    if "granada" in trevor["itens"]:
        print("Trevor usa uma granada")
        trevor["itens"].remove("granada")

        