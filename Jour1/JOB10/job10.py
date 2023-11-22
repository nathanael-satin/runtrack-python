montant_initial_de_linvestissement = float(input("Entrez le montant initial de l'invetissement : "))
taux_de_rendement_annuel = float(input("Entrez le taux de redendement annuel en pourcentage : "))
gain_annuel = montant_initial_de_linvestissement * (taux_de_rendement_annuel /100)
print (f"Montant Initial De L'invetissement : {montant_initial_de_linvestissement} euros")
print (f"Taux De Rendement Annuel  : {taux_de_rendement_annuel} %")
print (f"Gain Annuel : {gain_annuel:.2f} euros")
augmentation_capital = 5000
montant_initial_de_linvestissement += augmentation_capital
augmentation_taux =2 
taux_de_rendement_annuel += augmentation_taux
nouveau_gain_annuel = montant_initial_de_linvestissement * (taux_de_rendement_annuel /100)
print("/n Informations après augmentation du capital et du taux de rendement : ")
print(f" Montant Initial De L'invetissement : {montant_initial_de_linvestissement} euros")
print(f"Taux De Randement Annuel : {taux_de_rendement_annuel}%" )
print(f"Nouveau Gain Annuel : {nouveau_gain_annuel : .2f} euros")
retrait = 0.1 * montant_initial_de_linvestissement
montant_initial_de_linvestissement -= retrait
diminution_taux = 1
taux_de_rendement_annuel -= diminution_taux
montant_final = montant_initial_de_linvestissement * (1 + taux_de_rendement_annuel /100)
print("/n Informations après retrait et diminution du randement :")
print(f"Montant Final De L'invetissement : {montant_final : .2f} euros")
print(f"Taux De Rendement Annuel : { taux_de_rendement_annuel} %")