longueur = int (input("entrez un nombre"))
hauteur = int (input("entrez un nombre"))
x = " "
y = "-"
def tracer(longueur,hauteur):
    print (f"|{longueur*y}|")
    for i in range (2,hauteur,++1):
        print (f"|{longueur*x}|")
    print (f"|{longueur*y}|")

tracer(longueur,hauteur)       