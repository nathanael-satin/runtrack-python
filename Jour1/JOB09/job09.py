nom = "ps5"
prix = 500 
quantité = 2

print(f"Produit: {nom} \n Prix unitaire: {prix} \n stock {quantité}")
quantite_ajoutee = int(input("Entrez la quantité de produits à ajouter en stock : "))
quantité += quantite_ajoutee
print(quantité)
prix *= 1.1
print("\nInformations mises à jour du produit après ajout en stock et augmentation de prix ")
print(f"Nom du produit : {nom}")
print(f"Prix : {prix:.2f} euros") 
print(f"Quantité: {quantité}")