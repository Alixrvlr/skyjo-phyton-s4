import random

# Alix REVEILLERE, Ysaline MARTIN et Lise MIECKO


def verifColonne(listeJn,listeEtatCarte):
    for i in range(len(listeJn[0])):
        if listeJn[0][i]==listeJn[1][i] and listeJn[1][i]==listeJn[2][i] :
            if listeEtatCarte[0][i] == True and listeEtatCarte[1][i] == True and listeEtatCarte[2][i] == True:
                return True,i
    return False,None

def melangeCartes(listeCarteTrie):
    listePioche=[]
    for i in range (len(listeCarteTrie)):
        choix=random.choice(listeCarteTrie)
        listePioche.append(choix)
        listeCarteTrie.remove(choix)
    return listePioche


def convetirPosition(position,variableJeu):
    ligne = (position-1)//4
    colonne = (position-1)%4
    return ligne, colonne

def echangeCarte(listeJn,listeEtatCarteJn,carteJouer,position,variableJeu):
    ligne ,colonne =convetirPosition(position,variableJeu)
    print(ligne,colonne)
    print(listeJn)
    carteEnleve = listeJn[ligne][colonne]
    listeJn[ligne][colonne] = carteJouer
    listeEtatCarteJn[ligne][colonne] = True
    return listeJn, listeEtatCarteJn, carteEnleve


def totalPointJn(listeJn):
    s = 0
    for i in range(len(listeJn)):
        for j in range(len(listeJn[i])):
            s += listeJn[i][j]
    return s



def convertirJeuCartes3Tableau (listeJoueur):
    listeTrie =[]
    indice=0
    for i in range (3):
        L=[]
        for j in range(4):
            L.append(listeJoueur[indice])
            indice+=1
        listeTrie.append(L)
    return listeTrie

def supColonne (listeJn,listeEtatCatreJn,colonne):
    for i in range (3):
        listeJn[i][colonne]= 0
        listeEtatCatreJn[i][colonne]="0"

    return listeJn,listeEtatCatreJn


def recupPosition (x,y,variableJeu):        # Renvoie un chiffre entre 1 et 4 (ou pioche ou defausse) qui correspond au jeu dans lesquel on a cliqué (J1,J2,J3,J4)
    if x>=30 and x<= 345:
        if y>=10 and y<=335:
            return "jeu1"        # Jeu J1
        elif y>=370 and y<= 695:
            if variableJeu["nbJoueur"]==4:
                return "jeu4"        # Jeu J4
            else:
                return None
    
    elif x>=1010 and x<=1325:
        if y>=10 and y<=335:
            return "jeu2"        # Jeu J2
        elif y>=370 and y<= 695:
            if variableJeu["nbJoueur"]>= 3:
                return "jeu3"        # Jeu J3
            else :
                return None
        
    elif x>=598 and x<=673:
        if y>=315 and y<=420:
            return "pioche" #pioche
        
    elif x>=693 and x<=768:
        if y>=315 and y<=420:
            return "defausse" #defausse
        
    else:
        return None
        
def recupPositionCarte (x,y,decalageX,decalageY):
    if x-decalageX>=30 and x-decalageX<= 105:
        if y-decalageY>=10 and y-decalageY<=115:
            return 1        
        elif y-decalageY>=120 and y-decalageY<= 225:
            return 5 
        elif y-decalageY>=230 and y-decalageY<= 335:
            return 9
        
    elif x-decalageX>=110 and x-decalageX<= 185:
        if y-decalageY>=10 and y-decalageY<=115:
            return 2        
        elif y-decalageY>=120 and y-decalageY<= 225:
            return 6 
        elif y-decalageY>=230 and y-decalageY<= 335:
            return 10
        
    elif x-decalageX>=190 and x-decalageX<= 265:
        if y-decalageY>=10 and y-decalageY<=115:
            return 3        
        elif y-decalageY>=120 and y-decalageY<= 225:
            return 7 
        elif y-decalageY>=230 and y-decalageY<= 335:
            return 11
        
    elif x-decalageX>=270 and x-decalageX<= 345:
        if y-decalageY>=10 and y-decalageY<=115:
            return 4        
        elif y-decalageY>=120 and y-decalageY<= 225:
            return 8 
        elif y-decalageY>=230 and y-decalageY<= 335:
            return 12
    else :
        return None


def recupCoordonnéeCarte (x,y,decalageX,decalageY):
    if x-decalageX>=30 and x-decalageX<= 105:
        if y-decalageY>=10 and y-decalageY<=115:
            return 30+decalageX, 10+decalageY      
        elif y-decalageY>=120 and y-decalageY<= 225:
            return 30+decalageX, 120+decalageY
        elif y-decalageY>=230 and y-decalageY<= 335:
            return 30+decalageX, 230+decalageY
        
    elif x-decalageX>=110 and x-decalageX<= 185:
        if y-decalageY>=10 and y-decalageY<=115:
            return 110+decalageX, 10+decalageY   
        elif y-decalageY>=120 and y-decalageY<= 225:
            return  110+decalageX, 120+decalageY
        elif y-decalageY>=230 and y-decalageY<= 335:
            return  110+decalageX,230+decalageY
        
    elif x-decalageX>=190 and x-decalageX<= 265:
        if y-decalageY>=10 and y-decalageY<=115:
            return  190+decalageX, 10+decalageY      
        elif y-decalageY>=120 and y-decalageY<= 225:
            return  190+decalageX,120+decalageY 
        elif y-decalageY>=230 and y-decalageY<= 335:
            return  190+decalageX,230+decalageY
        
    elif x-decalageX>=270 and x-decalageX<= 345:
        if y-decalageY>=10 and y-decalageY<=115:
            return 270+decalageX, 10+decalageY        
        elif y-decalageY>=120 and y-decalageY<= 225:
            return 270+decalageX, 120+decalageY 
        elif y-decalageY>=230 and y-decalageY<= 335:
            return 270+decalageX, 230+decalageY
    else :
        return None
    
def retourneCarte(listeEtatCarteJn):
    for i in range (len(listeEtatCarteJn)):
        for j in range(len(listeEtatCarteJn)):
            if listeEtatCarteJn[i][j]==False:
                return False
    return True
        
def recupCoordoXColonneSup(colonne,decalageX):
    if colonne == 0:
        return 30+decalageX
    elif colonne ==1:
        return 110+decalageX
    elif colonne ==2:
        return 190+decalageX
    elif colonne ==3:
        return 270+decalageX
    else:
        return None
    

def verifFinJeu(joueur,listeEtatCarte):
    for i in range (len(listeEtatCarte)):
        for j in range (len(listeEtatCarte[0])):
            if listeEtatCarte[i][j]==False:
                return False
    return True

def chercheClassement (varibleJeu):
    totalscore=[]
    for jeu in varibleJeu["listeCarte"]:
        totalJ=0
        for i in range (len(jeu)):
            for j in range (len(jeu[0])):
                totalJ+=jeu[i][j]
        totalscore.append(totalJ)
    if varibleJeu["nbJoueur"]<3:
        totalscore[2]=145               # On met le score des joueur qui ne joue pas a 145 pour ne pas qu'il soit premier
    if varibleJeu["nbJoueur"]<4:
        totalscore[3]=145
    indiceJClassement=[]
    totalscoreChangement=list(totalscore)
    for k in range (varibleJeu["nbJoueur"]):
        joueur=totalscoreChangement.index(min(totalscoreChangement))
        totalscoreChangement[joueur]=145      # max du nombre de carte que l'on peut avoir+1 : carte 12 partout soit 12x12=144
        indiceJClassement.append(joueur)
    while len(indiceJClassement)<4:
        indiceJClassement.append(0)
    return indiceJClassement,totalscore