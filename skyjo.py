import random

def verifColonne(listeJn):
    for i in range(len(listeJn[0])):
        if listeJn[0][i]==listeJn[1][i] and listeJn[1][i]==listeJn[2][i] :
            return True,i
    return False

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
    listeJn[ligne][colonne] = carteJouer
    listeEtatCarteJn[ligne][colonne] = True
    return listeJn, listeEtatCarteJn

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