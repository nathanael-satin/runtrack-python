
chaine = "abcdefghijklmnopqrstuvwxyz"

def afficher_pyramide(chaine):
    longueur = len(chaine)


    for i in range(0, longueur+1):
        if i <= longueur:
            print(chaine[:i].ljust(longueur+1 - 0))
        else:
            print(chaine[:longueur+1 - i])


afficher_pyramide(chaine)