def vérifie_pair_impair(n):
   if isinstance(n, int):
        if n % 2 == 0:
            print("Le nombre est pair")
        else:
            print("Le nombre est impair")
   else:
        print("Le nombre n'est pas un entier")

vérifie_pair_impair(2)
vérifie_pair_impair(1)