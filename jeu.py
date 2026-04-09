from skyjo import *

# Alix REVEILLERE, Ysaline MARTIN et Lise MIECKO


# Fonction principal du déroulement du jeu
# X possibilitées pour etat qui permettent de savoir à quelle position du jeu nous sommes pour chaque joueru
#   - choix_pioche :            le joueur doit choisir de piocher, de prendre la carte dans la défausse ou de retourner une carte
#   - choix_carte :             le joueur doit choisir quelle carte il vaut retourner
#   - changement_carte :        la carte a été changé dans la liste du joueur et on attent l'affichage de cette carte dans l'interface
#   - attente_pop-up :          le joueur a choisi de piocher on attent l'affichage d'un pop-up sur l'interface pour que le joueur choisisse s'il veut jouer ou non cette carte
#   - start :                   le programme realise le fonction a faire avant de commencer (ex: distribuer les cartes)
#   - sup_colonne :             on supprime l'affiche de la colonne qui a été supprimé dans l'interface

def deroulerJeu(variableJeu):  
    
    if variableJeu["etat"] =='choix_pioche':    # le joueur choisi comment il veut jouer (pioche, défausse ou retourner carte)
        positionClic = recupPosition(variableJeu["position"][0],variableJeu["position"][1],variableJeu)         # on recupère la position du clic (dans un jeu, dans la pioche, dans la défausse, ou dans le vide)

        if positionClic != None:        # rentre que si le joueur n'a pas cliquer dans le vide

            if positionClic == 'pioche':
                variableJeu["typeJeu"] = positionClic
                variableJeu["etat"] = 'attente_pop-up'
            
            if positionClic == 'defausse':
                variableJeu["typeJeu"] = positionClic
                variableJeu["etat"] = 'choix_carte'
            
            # Si le joueur a bien cliqué dans son jeu et bien sur une carte (pas entre deux cartes), alors il peut retourner une carte
            elif positionClic == ("jeu"+str(variableJeu["joueur"]+1)) and recupPositionCarte(variableJeu["position"][0],variableJeu["position"][1],variableJeu["decalage"][variableJeu["joueur"]][0],variableJeu["decalage"][variableJeu["joueur"]][1]) != None :
                emplacementCarte=recupPositionCarte(variableJeu["position"][0],variableJeu["position"][1],variableJeu["decalage"][variableJeu["joueur"]][0],variableJeu["decalage"][variableJeu["joueur"]][1])        #on recupère la position de la carte choisi (1 à 12 ou None)
                ligne,colonne = convetirPosition(emplacementCarte,variableJeu)
                if not variableJeu["listeEtatCarte"][variableJeu["joueur"]][ligne][colonne]: # On verifie qu'il y ai bien une carte (pas une colonne supprimé (dans listeEtatCarte on a un "0" si la colonne est supprimé)) et quelle ne soit pas déjà retourné
                    variableJeu["listeEtatCarte"][variableJeu["joueur"]][ligne][colonne]= True  # On indique que la carte est retourné
                    variableJeu["nouvCarte"] = variableJeu["listeCarte"][variableJeu["joueur"]][ligne][colonne] # On enregistre la nouvelle carte pour son affichage
                    variableJeu["etat"]= 'changement_carte'
                    variableJeu["joueur"] =(variableJeu["joueur"]+1)%variableJeu["nbJoueur"]  # On change de joueur
                    variableJeu["changement_carte"]=True
 
  
      
    elif variableJeu["etat"] == 'choix_carte':  # le joueur choisi la carte qu'il veut retourner
        positionClic = recupPosition(variableJeu["position"][0],variableJeu["position"][1],variableJeu)
        # Si le joueur a bien cliqué dans son jeu et bien sur une carte (pas entre deux cartes), alors il peut retourner une carte
        if positionClic == ("jeu"+str(variableJeu["joueur"]+1)) and recupPositionCarte(variableJeu["position"][0],variableJeu["position"][1],variableJeu["decalage"][variableJeu["joueur"]][0],variableJeu["decalage"][variableJeu["joueur"]][1]) != None  :
            emplacementCarte=recupPositionCarte(variableJeu["position"][0],variableJeu["position"][1],variableJeu["decalage"][variableJeu["joueur"]][0],variableJeu["decalage"][variableJeu["joueur"]][1])        #position = int(input("choix position"))
            ligne,colonne = convetirPosition(emplacementCarte,variableJeu)  # On converti la position de la carte (entre 1 et 12) avec une ligne et une colonne pour pouvoir modifier les listes

            if variableJeu["listeEtatCarte"][variableJeu["joueur"]][ligne][colonne]!="0":

                if variableJeu["typeJeu"]=="pioche" :  # on verifie que la colonne n'est pas supprimé
                    if variableJeu["listeEtatCarte"][variableJeu["joueur"]][ligne][colonne]!="0":

                        cartePioche=variableJeu["pioche"].pop(0)    # on recupère la première carte de la pioche
            
                        if variableJeu["jouerCartePioche"] :    # True si le joueur veut jouer la carte de la pioche False sinon
                            emplacementCarte=recupPositionCarte(variableJeu["position"][0],variableJeu["position"][1],variableJeu["decalage"][variableJeu["joueur"]][0],variableJeu["decalage"][variableJeu["joueur"]][1])                  #position = int(input("choix position"))
                            variableJeu["listeCarte"][variableJeu["joueur"]],variableJeu["listeEtatCarte"][variableJeu["joueur"]],carteEnleve=echangeCarte(variableJeu["listeCarte"][variableJeu["joueur"]],variableJeu["listeEtatCarte"][variableJeu["joueur"]],cartePioche,emplacementCarte,variableJeu)
                            variableJeu["defausse"].insert(0,carteEnleve)   # On rajoute la carte remplacé dans la défausse
                            variableJeu["nouvCarte"] = cartePioche      # Carte à afficher
                            variableJeu["etat"]= 'changement_carte'
                        else :
                            variableJeu["defausse"].insert(0,cartePioche)   # on met dans la défausse la carte de la pioche car le joueur ne veut pas la joueur
                            variableJeu["typeJeu"] = "retourneCarte"
                            variableJeu["changement_carte"]=True


                if variableJeu["typeJeu"]=="defausse" and variableJeu["listeEtatCarte"][variableJeu["joueur"]][ligne][colonne]!="0":
                    if variableJeu["listeEtatCarte"][variableJeu["joueur"]][ligne][colonne]!="0":
                        carteDefausse = variableJeu["defausse"].pop(0) # On recupère la carte de la défausse pour la jouer
                        emplacementCarte=recupPositionCarte(variableJeu["position"][0],variableJeu["position"][1],variableJeu["decalage"][variableJeu["joueur"]][0],variableJeu["decalage"][variableJeu["joueur"]][1])        #position = int(input("choix position"))
                        variableJeu["listeCarte"][variableJeu["joueur"]],variableJeu["listeEtatCarte"][variableJeu["joueur"]],carteEnleve=echangeCarte(variableJeu["listeCarte"][variableJeu["joueur"]],variableJeu["listeEtatCarte"][variableJeu["joueur"]],carteDefausse,emplacementCarte,variableJeu)
                        variableJeu["nouvCarte"] = carteDefausse
                        variableJeu["defausse"].insert(0,carteEnleve)   # on met la carte remplacer dans la défausse
                        variableJeu["etat"]= 'changement_carte'
                        variableJeu["changement_carte"]=True

                # on retourne juste une carte du jeu quand le joueur ne veut pas jouer la carte de la pioche
                if variableJeu["typeJeu"]=="retourneCarte" and variableJeu["listeEtatCarte"][variableJeu["joueur"]][ligne][colonne]!="0":
                    emplacementCarte=recupPositionCarte(variableJeu["position"][0],variableJeu["position"][1],variableJeu["decalage"][variableJeu["joueur"]][0],variableJeu["decalage"][variableJeu["joueur"]][1])        #position = int(input("choix position"))
                    ligne,colonne = convetirPosition(emplacementCarte,variableJeu)
                    variableJeu["listeEtatCarte"][variableJeu["joueur"]][ligne][colonne]= True 
                    variableJeu["nouvCarte"] = variableJeu["listeCarte"][variableJeu["joueur"]][ligne][colonne]
                    variableJeu["etat"]= 'changement_carte'   
                    variableJeu["changement_carte"]=True
        

                variableJeu["joueur"] =(variableJeu["joueur"]+1)%variableJeu["nbJoueur"]  # on change de joueur


    if variableJeu["changement_carte"] and verifColonne(variableJeu["listeCarte"][(variableJeu["joueur"]-1)%variableJeu["nbJoueur"]],variableJeu["listeEtatCarte"][(variableJeu["joueur"]-1)%variableJeu["nbJoueur"]])[0] :     # si il y a une colonne avec les mêmes cartes
        colonneSup= verifColonne(variableJeu["listeCarte"][(variableJeu["joueur"]-1)%variableJeu["nbJoueur"]],variableJeu["listeEtatCarte"][(variableJeu["joueur"]-1)%variableJeu["nbJoueur"]])[1]
        carteColonneSup= variableJeu["listeCarte"][(variableJeu["joueur"]-1)%variableJeu["nbJoueur"]][0][colonne]
        variableJeu["listeCarte"][(variableJeu["joueur"]-1)%variableJeu["nbJoueur"]],variableJeu["listeEtatCarte"][(variableJeu["joueur"]-1)%variableJeu["nbJoueur"]]= supColonne(variableJeu["listeCarte"][(variableJeu["joueur"]-1)%variableJeu["nbJoueur"]], variableJeu["listeEtatCarte"][(variableJeu["joueur"]-1)%variableJeu["nbJoueur"]], colonne)
        variableJeu["liste_clonne_sup"]=[(variableJeu["joueur"]-1)%variableJeu["nbJoueur"],colonneSup]
        variableJeu["changement_carte"]=False
        for i in range (3):
            variableJeu["defausse"].insert(0,carteColonneSup)   
        variableJeu["etat"]='sup_colonne'


    return variableJeu       
