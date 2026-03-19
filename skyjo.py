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
    return ligne,colonne

def echangeCarte(listeJn,listeEtatCarteJn,carteJouer,position):
    ligne ,colonne =convetirPosition(position)
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


def recupPosition (x,y):        # Renvoie un chiffre entre 1 et 4 qui correspond au jeu dans lesquel on a cliqué (J1,J2,J3,J4)
    if x>=30 and x<= 345:
        if y>=10 and y<=335:
            return 1        # Jeu J1
        elif y>=370 and y<= 695:
            return 4        # Jeu J4
    
    elif x>=1010 and x<=1325:
        if y>=10 and y<=335:
            return 2        # Jeu J2
        elif y>=370 and y<= 695:
            return 3        # Jeu J3
        
    