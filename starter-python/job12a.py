import re
with open('data.txt', "r") as f:
    texte = f.read()
    paramtr = '[a-zA-Z]+'
    reg = re.findall(paramtr,texte)
    print(len(reg))