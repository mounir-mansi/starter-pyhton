import random

def jeux(tentatives):
    affichage = ""
    for l in mot:
        affichage = affichage + "_ "

    lettres_trouvees = ""
    lettres_proposees = ""
    while tentatives > 0:
        print ("nombre de vie", tentatives)
        print ("lettres proposées", lettres_proposees)
        print(affichage)
        proposition = input("Quelle lettre propose-tu ?: ")
        lettres_proposees = lettres_proposees + " " + proposition
        if proposition in mot:
            lettres_trouvees = lettres_trouvees + proposition
            print("-> Bien vu!")
        else:
            tentatives = tentatives - 1

        affichage = ""
        for x in mot:
            if x in lettres_trouvees:
                affichage += x + " "
            else:
                affichage += "_ "

        if "_" not in affichage:
            print(">>> Gagné! <<<")
            break
    print("    * Fin de la partie , vous avez perdu*    ")

mots = [""]
with open("dico_france.txt", "r", encoding="ISO-8859-1") as f:
    for l in f:
        mots.append(l.rstrip("\n"))
mot = random.choice(mots)
print(mot)


choix = int(input(
    "Bonjour, à quel niveau souhaites-tu jouer ?\n 1 debutant \n 2 intermediaire \n 3 expert \n1, 2 ou 3 ? "))

if choix == 1:

    tentatives = 10

    jeux(tentatives)

elif choix == 2:
    tentatives = 7

    jeux(tentatives)

elif choix == 3:
    tentatives = 4

    affichage = ""
    for l in mot:
        affichage = affichage + "_ "

    lettres_trouvees = ""
    lettres_proposees = ""
    while tentatives > 0:
        print ("nombre de vie", tentatives)
        print ("lettres proposées", lettres_proposees)
        print(affichage)
        proposition = input("Quelle lettre propose-tu ?: ")
        if proposition in mot:
            lettres_trouvees = lettres_trouvees + proposition
            print("-> Bien vu!")
        else:
            tentatives = tentatives - 1

        affichage = ""
        for x in mot:
            if x in lettres_trouvees:
                affichage += x + " "
            else:
                affichage += "_ "

        if "_" not in affichage:
            print(">>> Gagné! <<<")
            break
    print("    * Fin de la partie , vous avez perdu*    ")

else:
    print("nous n'avons pas compris votre choix")

# def length(liste):             # calculer le nombre de caractère d'une liste
#     nbr = 0
#     for i in liste :
#         nbr = nbr + 1
#     return nbr

# nbr_lettre = length(list(mot)) # pour séparer les mots en une liste de caracteres
# #print (nbr_lettre)