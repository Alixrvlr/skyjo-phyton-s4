import random

def verifColonne(listeJn):
    for i in range(len(listeJn[0])):
        if listeJn[0][i]==listeJn[1][i] and listeJn[1][i]==listeJn[2][i] :
            return True
    return False

def melangeCartes(listeCarteTrie):
    listePioche=[]
    for i in range (len(listeCarteTrie)):
        choix=random.choice(listeCarteTrie)
        listePioche.append(choix)
        listeCarteTrie.remove(choix)
    return listePioche

def echangeCarte(listeJn,listeEtatCarteJn,carteJouer,position):
    ligne = (position-1)//4
    colonne = (position-1)%4
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



