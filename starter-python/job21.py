def mySort(liste):
    permut = True
    passage = 0

    while permut == True :

        permut = False
        passage = passage + 1 

        for i in range (0 , len(liste)-passage):
            if liste[i] > liste[i+1]:
                permut = True
                liste[i], liste[i +1] =\ 
                liste[i +1], liste[i]
    return liste

def myDisplay(liste2):
    print(liste2)

myDisplay(mySort(15,685,695,69874,256))