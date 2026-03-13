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


