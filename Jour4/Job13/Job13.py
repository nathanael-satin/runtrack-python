def doublons_delete(liste):
    liste_unique = []
    for element in liste:
        if element not in liste_unique:
            liste_unique.append(element)
    return liste_unique
L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]


print("Liste De Base:", L)
L_doublons_delete = doublons_delete(L)

print("Liste doublons delete:", L_doublons_delete)
