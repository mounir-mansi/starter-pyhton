with open('domains.xml', "r") as f:
    cc = f.read()
a = cc.count('name="domain">')
print(a)
f.close()
