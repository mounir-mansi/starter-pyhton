nombre = int(input("entrer le nombre SVP: "))
with open('data.txt', "r") as f:
    texte = f.read()
    liste = texte.split()
nub = 0
for element in liste:
    if len(element) == nombre:
        nub = nub + 1
print(nub)