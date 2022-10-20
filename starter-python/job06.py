while input (">")!="Au revoir" :
    x = input (">")
    if x == "Bonjour" :
        print ("Bonjour à toi")
    elif (x!="Bonjour") and (x!="Au revoir"):
        print (x)
    elif x == "Au revoir":
        exit()
