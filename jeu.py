from skyjo import *

def deroulerJeu(variableJeu):  

    if variableJeu["etat"] =='choix_pioche':
        positionClic = recupPosition(variableJeu["position"][0],variableJeu["position"][1])
        emplacementCarte=recupPositionCarte(variableJeu["position"][0],variableJeu["position"][1],variableJeu["decalage"][variableJeu["joueur"]][0],variableJeu["decalage"][variableJeu["joueur"]][1])        #position = int(input("choix position"))

        
        if positionClic != None:
            if positionClic == 'pioche':
                variableJeu["typeJeu"] = positionClic
                variableJeu["etat"] = 'attente_pop-up'
            
            if positionClic == 'defausse':
                variableJeu["typeJeu"] = positionClic
                variableJeu["etat"] = 'choix_carte'
            
            elif positionClic == ("jeu"+str(variableJeu["joueur"]+1)) and recupPositionCarte(variableJeu["position"][0],variableJeu["position"][1],variableJeu["decalage"][variableJeu["joueur"]][0],variableJeu["decalage"][variableJeu["joueur"]][1]) != None :
                #variableJeu["typeJeu"] = 'retourneCarte'
                #variableJeu["etat"] = 'choix_carte'
                ligne,colonne = convetirPosition(emplacementCarte)
                if variableJeu["listeEtatCarte"][variableJeu["joueur"]][ligne][colonne]!= "0" :
                    variableJeu["listeEtatCarte"][variableJeu["joueur"]][ligne][colonne]= True 
                    variableJeu["nouvCarte"] = variableJeu["listeCarte"][variableJeu["joueur"]][ligne][colonne]
                    variableJeu["etat"]= 'changement_carte'
                    variableJeu["joueur"] =(variableJeu["joueur"]+1)%4
 
  
      
    elif variableJeu["etat"] == 'choix_carte':
        positionClic = recupPosition(variableJeu["position"][0],variableJeu["position"][1])

        if positionClic == ("jeu"+str(variableJeu["joueur"]+1)) and recupPositionCarte(variableJeu["position"][0],variableJeu["position"][1],variableJeu["decalage"][variableJeu["joueur"]][0],variableJeu["decalage"][variableJeu["joueur"]][1]) != None  :
            emplacementCarte=recupPositionCarte(variableJeu["position"][0],variableJeu["position"][1],variableJeu["decalage"][variableJeu["joueur"]][0],variableJeu["decalage"][variableJeu["joueur"]][1])        #position = int(input("choix position"))
            ligne,colonne = convetirPosition(emplacementCarte)
            if variableJeu["typeJeu"]=="pioche" and variableJeu["listeEtatCarte"][variableJeu["joueur"]][ligne][colonne]!="0":
                cartePioche=variableJeu["pioche"].pop(0)
                jouerCartePioche=variableJeu["jouerCartePioche"]
            
                if jouerCartePioche == True:     #if jouerCarte :
                    emplacementCarte=recupPositionCarte(variableJeu["position"][0],variableJeu["position"][1],variableJeu["decalage"][variableJeu["joueur"]][0],variableJeu["decalage"][variableJeu["joueur"]][1])                  #position = int(input("choix position"))
                    variableJeu["listeCarte"][variableJeu["joueur"]],variableJeu["listeEtatCarte"][variableJeu["joueur"]],carteEnleve=echangeCarte(variableJeu["listeCarte"][variableJeu["joueur"]],variableJeu["listeEtatCarte"][variableJeu["joueur"]],cartePioche,emplacementCarte)
                    variableJeu["defausse"].insert(0,carteEnleve)
                    variableJeu["nouvCarte"] = cartePioche
                    variableJeu["etat"]= 'changement_carte'
                else :
                    variableJeu["defausse"].insert(0,cartePioche)
                    variableJeu["typeJeu"] = "retourneCarte"


            if variableJeu["typeJeu"]=="defausse" and variableJeu["listeEtatCarte"][variableJeu["joueur"]][ligne][colonne]!="0":
                carteDefausse = variableJeu["defausse"].pop(0)
                emplacementCarte=recupPositionCarte(variableJeu["position"][0],variableJeu["position"][1],variableJeu["decalage"][variableJeu["joueur"]][0],variableJeu["decalage"][variableJeu["joueur"]][1])        #position = int(input("choix position"))
                variableJeu["listeCarte"][variableJeu["joueur"]],variableJeu["listeEtatCarte"][variableJeu["joueur"]],carteEnleve=echangeCarte(variableJeu["listeCarte"][variableJeu["joueur"]],variableJeu["listeEtatCarte"][variableJeu["joueur"]],carteDefausse,emplacementCarte)
                variableJeu["nouvCarte"] = carteDefausse
                variableJeu["defausse"].insert(0,carteEnleve)
                variableJeu["etat"]= 'changement_carte'





            if variableJeu["typeJeu"]=="retourneCarte" and variableJeu["listeEtatCarte"][variableJeu["joueur"]][ligne][colonne]!="0":
                emplacementCarte=recupPositionCarte(variableJeu["position"][0],variableJeu["position"][1],variableJeu["decalage"][variableJeu["joueur"]][0],variableJeu["decalage"][variableJeu["joueur"]][1])        #position = int(input("choix position"))
                ligne,colonne = convetirPosition(emplacementCarte)
                variableJeu["listeEtatCarte"][variableJeu["joueur"]][ligne][colonne]= True 
                variableJeu["nouvCarte"] = variableJeu["listeCarte"][variableJeu["joueur"]][ligne][colonne]
                variableJeu["etat"]= 'changement_carte'   


            # Verifier colonne
    

            variableJeu["joueur"] =(variableJeu["joueur"]+1)%4


    if verifColonne(variableJeu["listeCarte"][variableJeu["joueur"]-1],variableJeu["listeEtatCarte"][variableJeu["joueur"]-1])[0] == True:
        
        colonneSup= verifColonne(variableJeu["listeCarte"][variableJeu["joueur"]-1],variableJeu["listeEtatCarte"][variableJeu["joueur"]-1])[1]
        carteColonneSup= variableJeu["listeCarte"][variableJeu["joueur"]-1][0][colonne]
        variableJeu["listeCarte"][variableJeu["joueur"]-1],variableJeu["listeEtatCarte"][variableJeu["joueur"]-1]= supColonne(variableJeu["listeCarte"][variableJeu["joueur"]-1], variableJeu["listeEtatCarte"][variableJeu["joueur"]-1], colonne)
        variableJeu["liste_clonne_sup"]=[variableJeu["joueur"]-1,colonneSup]
        for i in range (3):
            variableJeu["defausse"].insert(0,carteColonneSup)
        variableJeu["etat"]='sup_colonne'


        
    #if "clic dans carte pioche":
    #    typeJeu = "pioche"
    #elif"clic dans carte défausse":
    #    typeJeu= "defausse"
    #elif "clic sur une des carte de son jeu":
    #    typeJeu ="retourneCarte"


    #typeJeu=int(input("1-piocher, 2-defausse, 3-retourner carte"))  #typeJeu = "retourneCarte"          #recuperer ce que le joueuer veut faire en fonction d'ou il clic

    #position = int(input("choix position"))            #recuperer l'endroit du clic



    return variableJeu       


"""def actionStart ():
    '''global joueur
    global listeJn
    global listeEtatCarteJn
    global nbJoueur
    global defausse
    global pioche'''
    
    

    # A faire qu'au premier tour
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
    
    #joueur=1

    variableJeu["etat"]= "choix_pioche"                     # Donne dans quel etat est le jeu (start,choix_pioche,choix_carte,changement_carte)
    variableJeu["joueur"]= 1                                # Donne le joueur auquel c'est le tour de jouer (de 1 à 4)
    variableJeu["listeCarte"]= listeJn                      # Liste des jeux de chaque joueur (le chiffre des cartes)
    variableJeu["listeEtatCarte"]= listeEtatCarteJn         # Liste des états des cartes de chaque jeu
    variableJeu["nbJoueur"]= nbJoueur                       # Nombre de joueur qui jouent
    variableJeu["defausse"]= defausse                       # Liste avec les cartes qui constituent la défausse
    variableJeu["pioche"]= pioche                           # Liste avec les cartes qui constituent la pioche
    #"typeJeu": None,                         # Donne le type de jeu choisi par le joueur (piocher,defausse,retourneCarte)
    #"nouvCarte": None,                     # Donne la nouvelle carte du jeu du joueur (pour l'affichage)
    #"position": None                        # Tuple avec les coordonnées du clic
    print(variableJeu["listeCarte"])
    return variableJeu"""


# Chaque joueur retourne deux avant de commencer
    
'''def retounerCartes()    :
    sommeJn=[0,0,0,0]
    
    print("Joueur",j+1)
    
    position=int(input(f"Position carte retourner{j+1}"))
    ligne,colonne=convetirPosition(position)
    listeEtatCarteJn[j][ligne][colonne]=True
    sommeJn[j]+=listeJn[j][ligne][colonne]

    joueurDebut=sommeJn.index(max(sommeJn))+1
    joueur=joueurDebut'''


'''def valideJouerCartePioche(variableJeu):
    variableJeu["jouerCartePioche"]=True
    return variableJeu'''