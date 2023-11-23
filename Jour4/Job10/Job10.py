L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
elements_filtres = [x for x in L if 25 <= x <= 90]
produit = 1
for element in elements_filtres:
    produit *= element
print(f"Liste: {L}")
print(f"Éléments dans l'intervalle [25, 90]: {elements_filtres}")
print(f"Produit des éléments dans l'intervalle [25, 90]: {produit}")
