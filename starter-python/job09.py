hauteur = int (input("entrez un nombre"))
x = " "
y = "_"
def triangle (hauteur):
    for i in range (1,hauteur,++1):
        print (f"{(hauteur-i)*x}/{int(i-1)*2*x}\\")
    print (f"/{(hauteur-1)*2*y}\\")
triangle(hauteur)