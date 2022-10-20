valeur1 = int (input ("entrez un nombre entier !"))
valeur2 = int (input ("entrez une deuxieme nombre entier!"))

if valeur1 < valeur2 :
    for i in range (valeur1+1,valeur2,++1):
        print (i)
elif valeur1 > valeur2 :
    for i in range (valeur1-1,valeur2,-1):
        print (i)
elif valeur1==valeur2:
    print ("valeurs égales")

