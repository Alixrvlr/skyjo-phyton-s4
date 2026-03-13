from skyjo import *

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

pioche = melangeCartes(cartes)

for i in range (12):
   listeJ1.append(pioche.pop(0))
   listeJ2.append(pioche.pop(0))
   listeJ3.append(pioche.pop(0))
   listeJ4.append(pioche.pop(0))

print(listeJ1)

print("")
listeJ1 = convertirJeuCartes3Tableau(listeJ1)
listeJ2 = convertirJeuCartes3Tableau(listeJ2)
listeJ3 = convertirJeuCartes3Tableau(listeJ3)
listeJ4 = convertirJeuCartes3Tableau(listeJ4)

gagner = False

while not gagner :
   joueur=1
   for i in range (nbJoueur):
        joueur +=1
        position = 1            #recuperer l'endroit du clic
        typeJeu = "piocher"          #recuperer ce que le joueuer veut faire en fonction d'ou il clic
       
        if typeJeu=="piocher" :
            jouerCarte = True                        # fonction qui affiche un pop up pour montrer la carte et 2 boutons sil veut garder cette carte et qui renvoi oui ou non
            if jouerCarte :
                position = 2                           #recuperer l'endroit du clic
                echangeCarte("listeJ"+str(joueur),"listeEtatCarteJ"+str(joueur),1,position)
            pass
      
        if typeJeu=="defausse" :
            pass
    
        if typeJeu=="retourneCarte" :
            pass
         
