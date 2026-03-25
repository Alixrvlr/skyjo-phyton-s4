import random

def verifColonne(listeJn):
    for i in range(len(listeJn[0])):
        if listeJn[0][i]==listeJn[1][i] and listeJn[1][i]==listeJn[2][i] :
            return True,i
    return False,None

def melangeCartes(listeCarteTrie):
    listePioche=[]
    for i in range (len(listeCarteTrie)):
        choix=random.choice(listeCarteTrie)
        listePioche.append(choix)
        listeCarteTrie.remove(choix)
    return listePioche


def convetirPosition(position):
    ligne = (position-1)//4
    colonne = (position-1)%4
    return ligne, colonne

def echangeCarte(listeJn,listeEtatCarteJn,carteJouer,position):
    ligne ,colonne =convetirPosition(position)
    print(ligne,colonne)
    print(listeJn)
    carteEnleve = listeJn[ligne][colonne]
    listeJn[ligne][colonne] = carteJouer
    listeEtatCarteJn[ligne][colonne] = True
    return listeJn, listeEtatCarteJn, carteEnleve

def recupPositionCarte(coordoClic,dicoCoordonneesJn):
    position=0
    for cle, valeur in dicoCoordonneesJn.items():
        if coordoClic == valeur :
            position = cle
    return position

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

def supColonne (listeJn,colonne):
    for i in range (3):
        listeJn[i][colonne]= 0

    return listeJn


def recupPosition (x,y):        # Renvoie un chiffre entre 1 et 4 (ou pioche ou defausse) qui correspond au jeu dans lesquel on a cliqué (J1,J2,J3,J4)
    if x>=30 and x<= 345:
        if y>=10 and y<=335:
            return "jeu1"        # Jeu J1
        elif y>=370 and y<= 695:
            return "jeu4"        # Jeu J4
    
    elif x>=1010 and x<=1325:
        if y>=10 and y<=335:
            return "jeu2"        # Jeu J2
        elif y>=370 and y<= 695:
            return "jeu3"        # Jeu J3
        
    elif x>=598 and x<=673:
        if y>=315 and y<=420:
            return "pioche" #pioche
        
    elif x>=693 and x<=768:
        if y>=315 and y<=420:
            return "defausse" #defausse
        
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
        
