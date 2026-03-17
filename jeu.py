from skyjo import *
def jeu (event):
    nbJoueur=4
    cartes =([-2]*5 +[0]*15 +[-1]*10 +[1]*10 +[2]*10 +[3]*10 +[4]*10 +[5]*10 +[6]*10 +[7]*10 +[8]*10 +[9]*10 +[10]*10 +[11]*10 +[12]*10)

    listeJ1 =[]
    listeJ2 =[]
    listeJ3 =[]
    listeJ4 =[]

    listeEtatCarteJ1 =[[False for i in range (4)] for i in range (3)]
    listeEtatCarteJ2 =[[False for i in range (4)] for i in range (3)]
    listeEtatCarteJ3 =[[False for i in range (4)] for i in range (3)]
    listeEtatCarteJ4 =[[False for i in range (4)] for i in range (3)]

    listeEtatCarteJn = [listeEtatCarteJ1,listeEtatCarteJ2,listeEtatCarteJ3,listeEtatCarteJ4]

    # Distribution des cartes
    pioche = melangeCartes(cartes)

    for i in range (12):
        listeJ1.append(pioche.pop(0))
        listeJ2.append(pioche.pop(0))
        listeJ3.append(pioche.pop(0))
        listeJ4.append(pioche.pop(0))



    print("")
    listeJ1 = convertirJeuCartes3Tableau(listeJ1)
    listeJ2 = convertirJeuCartes3Tableau(listeJ2)
    listeJ3 = convertirJeuCartes3Tableau(listeJ3)
    listeJ4 = convertirJeuCartes3Tableau(listeJ4)

    listeJn = [listeJ1,listeJ2,listeJ3,listeJ4]


    # On met la première carte dans la défausse
    defausse =[]
    defausse.append(pioche.pop(0))


    gagner = False
    print(listeJ1)


    # Chaque joueur retourne deux avant de commencer
    for i in range (4):
        pass


    while not gagner :
        joueur=0
        print("Joueur :",joueur+1)
        for i in range (nbJoueur):
            
            if "clic dans carte pioche":
                typeJeu = "pioche"
            elif"clic dans carte défausse":
                typeJeu= "defausse"
            elif "clic sur une des carte de son jeu":
                typeJeu ="retourneCarte"



            position = int(input("choix position"))            #recuperer l'endroit du clic
            typeJeu = "retourneCarte"          #recuperer ce que le joueuer veut faire en fonction d'ou il clic
        



            if typeJeu=="piocher" :
                jouerCarte = True                        # fonction qui affiche un pop up pour montrer la carte et 2 boutons sil veut garder cette carte et qui renvoi oui ou non
                cartePioche=pioche.pop(0)
                if jouerCarte :
                    #position = 2                           #recuperer l'endroit du clic
                    listeJn[joueur],listeEtatCarteJn[joueur]=echangeCarte(listeJn[joueur],listeEtatCarteJn[joueur],cartePioche,position)
                else :
                    defausse.insert(0,cartePioche)
                    typeJeu = "retourneCarte"
        




            if typeJeu=="defausse" :
                carteDefausse = defausse.pop(0)
                if jouerCarte :
                    #position = 2                           #recuperer l'endroit du clic
                    listeJn[joueur],listeEtatCarteJn[joueur]=echangeCarte(listeJn[joueur],listeEtatCarteJn[joueur],carteDefausse,position)
                else :
                    defausse.insert(0,cartePioche)
                    typeJeu = "retourneCarte"





            if typeJeu=="retourneCarte" :
                
                ligne,colonne = convetirPosition(position)
                listeEtatCarteJn[joueur][ligne][colonne]= True


            # Verifier colonne
            if verifColonne[0] == True:
                listeJn[joueur]= supColonne(listeJn[joueur],verifColonne[1])

            print(listeJn[joueur])
            print(listeEtatCarteJn[joueur])
            joueur +=1
            

