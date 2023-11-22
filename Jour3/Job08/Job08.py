def Panier(type , saison):
    if type  == "fruits" and saison=="hiver":
        print("orange, mandarine et kiwi")
    if type =="fruits" and saison =="été":
        print("Poire, fraise, cassis")
    if type =="legume" and saison =="hiver":
        print("carotte, topinambour, endive")    
    elif type =="legume" and saison =="été":
        print("artichaut, aubergine,navet")    
Panier ("fruits" , "été")

