valeur1 = int (input ("entrez un nombre entier !"))
valeur2 = int (input ("entrez une deuxieme nombre entier!"))

if valeur1 < valeur2 :
    x = valeur1 + 1
    while valeur1 < x < valeur2 :
        print (x)
        x = x + 1
elif valeur1 > valeur2 :
    x = valeur1 - 1
    while valeur2 < x < valeur1 :
        print (x)
        x = x - 1
elif valeur1==valeur2:
    print ("valeurs égales")

