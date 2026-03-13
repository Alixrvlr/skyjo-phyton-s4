import random

def verifColonne(J):
    for i in range(len(J)):
        if J[0][i]==J[1][i] and J[1][i]==J[2][i] and J[2][i]==J[3][i]:
            return True
    return False

def melangeCartes(CarteTrie):
    pioche=[]
    for i in range (len(CarteTrie)):
        choix=random.choice(CarteTrie)
        pioche.append(choix)
        CarteTrie.remove(choix)
    return pioche

def echangeCarte(J,EtatCarteJ,cartejouer,position):
    J[position]=cartejouer
    EtatCarteJ[position]=True
    return J, EtatCarteJ

def recupPositionCarte(coordoClic,dicoCoordonneesJ):
    if coordoClic in dicoCoordonneesJ:
        pass


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