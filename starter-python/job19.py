def myFonction(*int):
    myList = int

    permut = True
    passage = 0

    while permut == True :

        permut = False
        passage = passage + 1 

        for i in range (0 , len(myList)-passage):
            if myList[i] > myList[i+1]:
                permut = True
                myList[i], myList[i +1] =\ 
                myList[i +1], myList[i]
    print (myList)

myFonction(1568,2446,6565,36,94,4456)







#def sorting(list) :
#   for i in list :
#       mini=min(list)   
#       list.remove(mini)
#       list.append(mini)
#   print (list)
liste_entier(2335,2545,25,25,55,65)
sorting(liste_entier(2335,2545,25,25,55,65))