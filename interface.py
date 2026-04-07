from tkinter import *
from tkinter import ttk
from jeu import *
from skyjo import *
import winsound 


# Fichier Interface Graphique du jeu - projet S4 informatique
# Alix REVEILLERE, Ysaline MARTIN et Lise MIECKO

''' Création de la fenêtre ----------------------------------------------------------------------------------------'''

fenetrePrincipale = Tk()
fenetrePrincipale.title("Skyjo")
fenetrePrincipale.iconbitmap("eseoLogo.ico")

largeur = fenetrePrincipale.winfo_screenwidth()
hauteur = fenetrePrincipale.winfo_screenheight()

# la fenêtre prend tout l'écran
fenetrePrincipale.geometry(f"{largeur}x{hauteur}+0+0")




''' Création du plateau du jeu ---------------------------------------------------------------------------------------'''

# Délimitations du plateau de jeu 
# width=fenetre.winfo_screenwidth() = 1366
# height= 710

# Délimitations d'un paquet de cartes de joueur
# Espacement des cartes = 5  

# Délimitation d'une carte 
# width = 75
# height = 290//3 = 105

# width/2 = 683
# height/2 = 355



# frame pour l'interface du jeu

frameJeu = Frame(fenetrePrincipale, background='#000000')
can = Canvas(frameJeu, bg ='black')
can.place(anchor="nw", width=fenetrePrincipale.winfo_screenwidth(), height=745, x=0, y=0)

# frame pour l'interface du menu

frameMenu = Frame(fenetrePrincipale, background="#1BB5E4")

# frame pour l'affichage des scores

frameScore = Frame(fenetrePrincipale, background="#1BB5E4")


    



''' Cartes -------------------------------------------------------------------------------------------------'''


images=[]
imagesPopUp=[]
fleche=[]

def affichagecarteJnRecto(variableJeu):
    for j in range (4):
        versocarte=PhotoImage(file="img/verso.png")#.subsample(3)
        x=[30,30,30,110,110,110,190,190,190,270,270,270]
        y=[10,120,230,10,120,230,10,120,230,10,120,230]
        for i in range (12):
            can.create_image(x[i]+variableJeu["decalage"][j][0]+75/2, y[i]+variableJeu["decalage"][j][1]+105/2, image=versocarte)
        images.append(versocarte)

def affichagepioche(cartePioche):
    listeImgCarteVerso=["img/-2.png","img/-1.png","img/0.png","img/1.png","img/2.png","img/3.png","img/4.png","img/5.png","img/6.png","img/7.png","img/8.png","img/9.png","img/10.png","img/11.png","img/12.png"]
    pioche=PhotoImage(file="img/verso.png")
    defausse=PhotoImage(file=listeImgCarteVerso[cartePioche+2])
    can.create_image(598+75/2,315+105/2,image=pioche)
    can.create_image(693+75/2,315+105/2,image=defausse)
    images.append(pioche)
    images.append(defausse)

def affichagepiochePopUp(cartePioche,canvas):
    listeImgCarteVerso=["img/-2.png","img/-1.png","img/0.png","img/1.png","img/2.png","img/3.png","img/4.png","img/5.png","img/6.png","img/7.png","img/8.png","img/9.png","img/10.png","img/11.png","img/12.png"]
    pioche=PhotoImage(file=listeImgCarteVerso[cartePioche+2])
    canvas.create_image(140+75/2,315+195/2,image=pioche)
    canvas.image =pioche        #images.append(pioche)


def affichageCarteVerso (carte,x,y,decalagex,decalagey):
    global images
    listeImgCarteVerso=["img/-2.png","img/-1.png","img/0.png","img/1.png","img/2.png","img/3.png","img/4.png","img/5.png","img/6.png","img/7.png","img/8.png","img/9.png","img/10.png","img/11.png","img/12.png"]
    carte = PhotoImage(file=listeImgCarteVerso[carte+2])
    can.create_image(x+75/2, y+105/2, image=carte)      #can.create_image(x+a+75/2, y+b+105/2, image=carte)
    images.append(carte)
    
def affichageCarreNoire(x,y):
    can.create_rectangle(x,y,x+75,y+105, width=1,fill="#000000")

def affichageColonneSup(variableJeu) :
    joueur = variableJeu["liste_clonne_sup"][0]
    colonne= variableJeu["liste_clonne_sup"][1]
    xCoin= recupCoordoXColonneSup(colonne, variableJeu["decalage"][variableJeu["joueur"]-1][0])

    for i in range (3):
        affichageCarreNoire(xCoin, 10+i*110+variableJeu["decalage"][variableJeu["joueur"]-1][1])







''' Affichage joueur et instructions -----------------------------------------------------------------------------------------'''


def instructionJeuJn(variableJeu) :
    global fleche
    # variableJeu["joueur"] = (de 0 à 3 : +1 pour le vrai numéro)


    numeroJn = variableJeu["joueur"] + 1
    nomJoueur.config(text = "C'est au tour du joueur " + str(numeroJn))
    

    instructionRetourner2Carte.place_forget()
    instruction_PlacerCarte.place_forget()
    instruction_ChoixCarteRetourner.place_forget()

    nomJoueur.place(anchor="center", x = 680, y = 60)
    instruction_option.place(anchor="center", x = 680, y = 150)
    instruction_piocherCarte.place(anchor="center", x = 680, y = 220)

    if numeroJn == 1 :
        flecheDroite.place_forget()  # caché 
        flecheGauche.place_forget()
        flecheGauche.place(anchor="w", x = 350, y = 175)

    elif numeroJn == 2 :
        flecheDroite.place_forget()  # caché 
        flecheGauche.place_forget()
        #flecheGauche.destroy()
        flecheDroite.place(anchor="e", x = 1000, y = 175)

    elif numeroJn == 3 :
        flecheDroite.place_forget()  # caché 
        flecheGauche.place_forget()
        flecheDroite.place(anchor="e", x = 1000, y = 530)

    else :
        flecheDroite.place_forget()  # caché 
        flecheGauche.place_forget()
        flecheGauche.place(anchor="w", x = 350, y = 530) 




def instructionPlacerCarteJn(variableJeu) :

    # variableJeu["joueur"] = (de 0 à 3 : +1 pour le vrai numéro)

    numeroJn = variableJeu["joueur"] + 1
    nomJoueur.config(text = "C'est au tour du joueur " + str(numeroJn))

    # effacer les autres textes

    instructionRetourner2Carte.place_forget()
    instruction_option.place_forget()
    instruction_piocherCarte.place_forget()
    instruction_ChoixCarteRetourner.place_forget()


    # placer les phrases/flèches sur l'écran

    nomJoueur.place(anchor="center", x = 680, y = 60)
    instruction_PlacerCarte.place(anchor="center", x = 680, y = 150)

    if numeroJn == 1 :
        flecheDroite.place_forget()  # caché 
        flecheGauche.place_forget()
        flecheGauche.place(anchor="w", x = 350, y = 175)

    elif numeroJn == 2 :
        flecheDroite.place_forget()  # caché 
        flecheGauche.place_forget()
        #flecheGauche.destroy()
        flecheDroite.place(anchor="e", x = 1000, y = 175)

    elif numeroJn == 3 :
        flecheDroite.place_forget()  # caché 
        flecheGauche.place_forget()
        flecheDroite.place(anchor="e", x = 1000, y = 530)

    else :
        flecheDroite.place_forget()  # caché 
        flecheGauche.place_forget()
        flecheGauche.place(anchor="w", x = 350, y = 530) 



def instructionChoisirEmplacementCarteJn(variableJeu) :

    # variableJeu["joueur"] = (de 0 à 3 : +1 pour le vrai numéro)

    numeroJn = variableJeu["joueur"] + 1
    nomJoueur.config(text = "C'est au tour du joueur " + str(numeroJn))

    # effacer textes

    instruction_option.place_forget()
    instruction_piocherCarte.place_forget()
    instruction_PlacerCarte.place_forget()
    instructionRetourner2Carte.place_forget()

    # placer les phrases sur l'écran

    nomJoueur.place(anchor="center", x = 680, y = 60)
    instruction_ChoixCarteRetourner.place(anchor="center", x = 680, y = 150)

    if numeroJn == 1 :
        flecheDroite.place_forget()  # caché 
        flecheGauche.place_forget()
        flecheGauche.place(anchor="w", x = 350, y = 175)

    elif numeroJn == 2 :
        flecheDroite.place_forget()  # caché 
        flecheGauche.place_forget()
        #flecheGauche.destroy()
        flecheDroite.place(anchor="e", x = 1000, y = 175)

    elif numeroJn == 3 :
        flecheDroite.place_forget()  # caché 
        flecheGauche.place_forget()
        flecheDroite.place(anchor="e", x = 1000, y = 530)

    else :
        flecheDroite.place_forget()  # caché 
        flecheGauche.place_forget()
        flecheGauche.place(anchor="w", x = 350, y = 530) 




def instructionRetournerCarteDebutJn(variableJeu) :
    
    # affiche quel joueur doit piocher 2 cartes (seulement en début de partie)

    numeroJn = variableJeu["joueur"] + 1
    nomJoueur.config(text = "C'est au tour du joueur " + str(numeroJn))
    

    # effacer les autres textes

    instruction_option.place_forget()
    instruction_piocherCarte.place_forget()
    instruction_PlacerCarte.place_forget()
    instruction_ChoixCarteRetourner.place_forget()


    # placer les phrases sur l'écran

    nomJoueur.place(anchor="center", x = 680, y = 60)
    instructionRetourner2Carte.place(anchor="center", x = 680, y = 180)


    if numeroJn == 1 :
        flecheDroite.place_forget()  # caché 
        flecheGauche.place_forget()
        flecheGauche.place(anchor="w", x = 350, y = 175)

    elif numeroJn == 2 :
        flecheDroite.place_forget()  # caché 
        flecheGauche.place_forget()
        #flecheGauche.destroy()
        flecheDroite.place(anchor="e", x = 1000, y = 175)

    elif numeroJn == 3 :
        flecheDroite.place_forget()  # caché 
        flecheGauche.place_forget()
        flecheDroite.place(anchor="e", x = 1000, y = 530)

    else :
        flecheDroite.place_forget()  # caché 
        flecheGauche.place_forget()
        flecheGauche.place(anchor="w", x = 350, y = 530) 






''' Déroulé du jeu -------------------------------------------------------------------------------------------------'''

def actionStart ():
    
    variableJeu = {}

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


    # Pour teste :
    listeJn[0]=[[4,6,7,7],[4,5,9,3],[4,7,7,1]]
    listeJn[1]=[[4,6,7,7],[4,5,9,3],[4,7,7,1]]
    listeJn[2]=[[4,6,7,7],[4,5,9,3],[4,7,7,1]]
    listeJn[3]=[[4,6,7,7],[4,5,9,3],[4,7,7,1]]
    
    gagner = False
    

    variableJeu["etat"]= "start"                     # Donne dans quel etat est le jeu (start,choix_pioche,choix_carte,changement_carte)
    variableJeu["joueur"]= 0                                # Donne le joueur auquel c'est le tour de jouer (de 0 à 3 (+1 pour avoir le vrai numéro de joueur))
    variableJeu["listeCarte"]= listeJn                      # Liste des jeux de chaque joueur (le chiffre des cartes)
    variableJeu["listeEtatCarte"]= listeEtatCarteJn         # Liste des états des cartes de chaque jeu
    variableJeu["nbJoueur"]= nbJoueur                       # Nombre de joueur qui jouent
    variableJeu["defausse"]= defausse                       # Liste avec les cartes qui constituent la défausse
    variableJeu["pioche"]= pioche                           # Liste avec les cartes qui constituent la pioche
    variableJeu["nbCarteRetourner"]=0                       # Pour les 2 carte par joueur à retourner au debut
    variableJeu["decalage"]= [[0,0],[980,0],[980,360],[0,360]]   # décalage des coordonnées des positions des jeux en fonction du joueur
    variableJeu["sommeCarteRetourne"]=[0,0,0,0]             # pour savoir quel joueur commence
    variableJeu["dernierJoueur"]=None                       # on ne sait pas encore quel est le dernier joueur on met None pour quand même faire le teste
    variableJeu["jeuTermine"]=False
    #"typeJeu": None,                         # Donne le type de jeu choisi par le joueur (piocher,defausse,retourneCarte)
    #"nouvCarte": None,                     # Donne la nouvelle carte du jeu du joueur (pour l'affichage)
    #"position": None                        # Tuple avec les coordonnées du clic
    print(variableJeu["listeCarte"])
    affichagecarteJnRecto(variableJeu)
    affichagepioche(variableJeu["defausse"][0])
    return variableJeu



def retournerCarteDebut (x,y,variableJeu):
    
    
    
    ligne,colonne=convetirPosition(recupPositionCarte(x,y,variableJeu["decalage"][(variableJeu["joueur"])%4][0],variableJeu["decalage"][(variableJeu["joueur"])%4][1]))
    variableJeu["listeEtatCarte"][variableJeu["joueur"]][ligne][colonne]=True
    variableJeu["sommeCarteRetourne"][variableJeu["joueur"]]+=variableJeu["listeCarte"][variableJeu["joueur"]][ligne][colonne]

    xcoin,ycoin= recupCoordonnéeCarte(x,y,variableJeu["decalage"][(variableJeu["joueur"])%4][0],variableJeu["decalage"][(variableJeu["joueur"])%4][1])
    affichageCarteVerso(variableJeu["listeCarte"][variableJeu["joueur"]][ligne][colonne],xcoin,ycoin)
    variableJeu["nbCarteRetourner"]+=1

    if variableJeu["nbCarteRetourner"]%2==0:
        variableJeu["joueur"]+=1
        if variableJeu["joueur"]<4:
            instructionRetournerCarteDebutJn(variableJeu)

    if variableJeu["nbCarteRetourner"]==2*variableJeu["nbJoueur"]:
        joueurDebut=variableJeu["sommeCarteRetourne"].index(max(variableJeu["sommeCarteRetourne"]))
        variableJeu["joueur"]=joueurDebut
        variableJeu["etat"]='choix_pioche'

    if variableJeu["nbCarteRetourner"] == 2*variableJeu["nbJoueur"]:
        instructionJeuJn(variableJeu)




''' Fonction Rejouer ----------------------------------------------------------------------------------------'''

#Fonction pour remettre le jeu a zero

def rejouer ():
    pass





'''fonction son-----------------------------------------------------------------------------------------------------'''

def son():
    winsound.PlaySound("son_background.wav", winsound.SND_ASYNC | winsound.SND_LOOP)


def stop_son():
    winsound.PlaySound(None, winsound.SND_PURGE)




''' Fenêtre Pop-Up pour montrer la carte piochée -------------------------------------------------------------------'''

def popupChoix(variableJeu) :
    def valideJouerCartePioche():
        variableJeu["jouerCartePioche"]=True
        instructionPlacerCarteJn(variableJeu)
        miniFenetre.destroy()
    
    def invalideJouerCartePioche():
        variableJeu["jouerCartePioche"]=False
        instructionChoisirEmplacementCarteJn(variableJeu)
        miniFenetre.destroy()
    

    messagePioche = "Vous avez pioché un"
    messageChoix = "Voulez-vous jouer cette carte ?"
    miniFenetre = Toplevel()
    miniFenetre.iconbitmap("eseoLogo.ico")
    miniFenetre.config(background='white')
    miniFenetre.title('Choix')
    miniFenetre.geometry("300x380+525+180") # dimensions et position de la fenêtre
    message1 = Label(miniFenetre, text=messagePioche, fg="black", bg="white", font='Selestin 15')
    message2 = Label(miniFenetre, text=messageChoix, fg="black", bg="white", font='Selestin 15')


    # emplacement de la carte
    # largeur = 125
    # hauteur = 175
    carte = Canvas(miniFenetre, width=150, height=210)
    #affichagepiochePopUp(variableJeu['pioche'][0],carte)
    listeImgCarteVerso=["img/-2.png","img/-1.png","img/0.png","img/1.png","img/2.png","img/3.png","img/4.png","img/5.png","img/6.png","img/7.png","img/8.png","img/9.png","img/10.png","img/11.png","img/12.png"]
    pioche=PhotoImage(file=listeImgCarteVerso[variableJeu['pioche'][0]+2])
    pioche = pioche.zoom(2, 2)          # On zoom l'image pour qu'elle remplisse tout le canvas
    carte.create_image(150/2,210/2,image=pioche)
    imagesPopUp.append(pioche)


    # boutons
    oui = Button(miniFenetre, text ='Oui', command= valideJouerCartePioche)
    non = Button(miniFenetre, text ='Non', command= invalideJouerCartePioche)


    # placer sur l'écran
    message1.grid(row=1, column=0, sticky="n", padx = 1, pady = 10)
    carte.grid(row=2, column=0, sticky="n", padx = 5, pady = 10)
    message2.grid(row=4, column=0, sticky="n", padx = 10, pady = 10)
    oui.grid(row=6, column=0, sticky="w", padx = 5, pady = 5)
    non.grid(row=6, column=0, sticky="e", padx = 5, pady = 5)


    variableJeu["etat"]='choix_carte'

    return variableJeu





''' Fenêtre popup pour annoncer les scores ---------------------------------------------------------------------------------'''

def fenetreScore(vainqueur, sVainqueur, deuxieme, sDeuxieme, troisieme=0, sTroisieme=0, quatrieme=0, sQuatrieme=0) :
    

    # messages    
    messageBravo = "Bravo ! " 
    messageVainqueur = vainqueur + " a gagné cette partie avec un score de " + str(sVainqueur) + " points"
    message2e = deuxieme + " a fini avec " + str(sDeuxieme) + " points"
    
    if troisieme != 0 : # il y a un troisième joueur
        message3e = troisieme + " a fini avec " + str(sTroisieme) + " points"
    
    if quatrieme != 0 : # il y a un quatrième joueur
        message4e = quatrieme + " a fini avec " + str(sQuatrieme) + " points"
    
    message1 = Label(frameScore, text=messageBravo, fg="black", bg="white", font='Selestin 15')
    message2 = Label(frameScore, text=messageVainqueur, fg="black", bg="white", font='Selestin 15')
    message3 = Label(frameScore, text=message2e, fg="black", bg="white", font='Selestin 13')
    
    if troisieme != 0 : 
        message4 = Label(frameScore, text=message3e, fg="black", bg="white", font='Selestin 13')
    
    if quatrieme != 0 :
        message5 = Label(frameScore, text=message4e, fg="black", bg="white", font='Selestin 13')

    # placer sur l'écran
    message1.grid(row=1, column=2, sticky="n", padx = 10, pady = 10)
    message2.grid(row=2, column=2, sticky="n", padx = 10, pady = 10)
    message3.grid(row=4, column=2, sticky="n", padx = 10, pady = 10)
    
    if troisieme != 0 : 
        message4.grid(row=5, column=2, sticky="n", padx = 10, pady = 10)
    
    if quatrieme != 0 :
        message5.grid(row=6, column=2, sticky="n", padx = 10, pady = 10)

    winsound.PlaySound("son_victoire.wav", winsound.SND_ASYNC )


def popupScore(vainqueur, sVainqueur, deuxieme, sDeuxieme, troisieme=0, sTroisieme=0, quatrieme=0, sQuatrieme=0) :
    
    # nom 1er, scoreVainqueur, nom 2e, score 2e...

    fenetreFin = Toplevel()
    fenetreFin.iconbitmap("eseoLogo.ico")
    fenetreFin.config(background="#5ab4c9")
    fenetreFin.title('Fin de la partie')
    fenetreFin.geometry("525x250+420+250") # dimensions et position de la fenêtre

    # messages    
    messageBravo = "Bravo ! " 
    messageVainqueur = vainqueur + " a gagné cette partie avec un score de " + str(sVainqueur) + " points"
    message2e = deuxieme + " a fini avec " + str(sDeuxieme) + " points"
    
    if troisieme != 0 : # il y a un troisième joueur
        message3e = troisieme + " a fini avec " + str(sTroisieme) + " points"
    
    if quatrieme != 0 : # il y a un quatrième joueur
        message4e = quatrieme + " a fini avec " + str(sQuatrieme) + " points"
    
    message1 = Label(fenetreFin, text=messageBravo, fg="black", bg="#5ab4c9", font='Selestin 15')
    message2 = Label(fenetreFin, text=messageVainqueur, fg="black", bg="#5ab4c9", font='Selestin 15')
    message3 = Label(fenetreFin, text=message2e, fg="black", bg="#5ab4c9", font='Selestin 13')
    
    if troisieme != 0 : 
        message4 = Label(fenetreFin, text=message3e, fg="black", bg="#5ab4c9", font='Selestin 13')
    
    if quatrieme != 0 :
        message5 = Label(fenetreFin, text=message4e, fg="black", bg="#5ab4c9", font='Selestin 13')

    # placer sur l'écran
    message1.grid(row=1, column=0, sticky="n", padx = 10, pady = 10)
    message2.grid(row=2, column=0, sticky="n", padx = 10, pady = 10)
    message3.grid(row=4, column=0, sticky="n", padx = 10, pady = 10)
    
    if troisieme != 0 : 
        message4.grid(row=5, column=0, sticky="n", padx = 10, pady = 10)
    
    if quatrieme != 0 :
        message5.grid(row=6, column=0, sticky="n", padx = 10, pady = 10)
    winsound.PlaySound("son_victoire.wav", winsound.SND_ASYNC )


#popupScore("Joueur 1", 12, "Joueur 4", 20, "Joueur 3", 33, "Joueur 2", 50)



''' Fenêtre Menu -----------------------------------------------------------------------------------------------------------'''


def vider() :
    # vider les Entry des noms des joueurs
    cadreNomJ1.delete(0, END)
    cadreNomJ2.delete(0, END)
    cadreNomJ3.delete(0, END)
    cadreNomJ4.delete(0, END)


def retournerAuMenu() :
    frameJeu.pack_forget()
    vider()
    frameMenu.pack(fill="both", expand=True)

def test() :
    frameJeu.pack_forget()
    vider()
    frameScore.pack(fill="both", expand=True)


def valider() :
    frameMenu.pack_forget() # permet de cacher la Frame du menu
    frameJeu.pack(fill="both", expand=True) # permet d'afficher la Frame du jeu




def fenetreMenu(variableJeu) :

    #Création des éléments à afficher 

    options = ["2" , "3" , "4"]
    choixNbJoueurs = ttk.Combobox(frameMenu, values=options)

    blanc.grid(row=0, column=0, sticky=E, padx = 10, pady = 10)
    # Utilisation de la méthode grid () pour positionner les éléments
    titre.grid(row=1, column=3, columnspan=3)


    labListe.grid(row=2, column=0, sticky=E, padx = 10, pady = 10)

    nomJ1.grid(row=3, column=0, sticky=E, padx = 5, pady = 10)
    nomJ2.grid(row=4, column=0, sticky=E, padx = 5, pady = 10)
    nomJ3.grid(row=5, column=0, sticky=E, padx = 5, pady = 10)
    nomJ4.grid(row=6, column=0, sticky=E, padx = 5, pady = 10)

    choixNbJoueurs.grid(row = 2, column=1, padx = 10, pady = 10)

    cadreNomJ1.grid(row=3, column=1, sticky=E, padx = 5, pady = 10)
    cadreNomJ2.grid(row=4, column=1, sticky=E, padx = 5, pady = 10)
    cadreNomJ3.grid(row=5, column=1, sticky=E, padx = 5, pady = 10)
    cadreNomJ4.grid(row=6, column=1, sticky=E, padx = 5, pady = 10)




    bValider.grid(row=10,column=0)
    bVider.grid(row=10,column=1)
    bQuitter.grid(row=10, column=2)
    #frameJeu.forget()
    #frameMenu.pack()




def popupMenu(callback):#variableJeu
    #global nomJoueurs
    nomJoueurs=[]
    variableJeu["listeNomJoueur"]=nomJoueurs
    def validerNom():
        #nomJoueurs=[]
        nomJoueurs.clear()
        for entry in entriesJoueurs :
            nomJoueurs.append(entry.get())
        variableJeu["listeNomJoueur"]=nomJoueurs
        callback(nomJoueurs)
        
        
    # Création de la fenêtre
    fenetreMenu = Toplevel()
    fenetreMenu.iconbitmap("eseoLogo.ico")
    fenetreMenu.config(background="#5ab4c9")
    fenetreMenu.title('Menu')
    fenetreMenu.geometry("800x600+250+50") # dimensions et position de la fenêtre
    fenetreMenu.grid_columnconfigure

    # Titre de la fenêtre
    message1 = Label(fenetreMenu, text="Menu", fg="black", bg="#5ab4c9", font='Selestin 15')
    message1.grid(row=0, column=0, sticky="n", padx = 10, pady = 10)

    # Création des zones d'entrée
    entriesJoueurs = []
    for i in range (4):      #variableJeu["nbJoueur"]

        frameJoueur = Frame(fenetreMenu, background='#3396ff')
        Prenom = Label(frameJoueur, text="Joueur "+str(i+1),  background='#3396ff', fg="#ffffff")
        champPrenom = Entry(frameJoueur, bg="#ffffff", fg="green", font="Courier", bd=5, justify=CENTER)
        Prenom.grid(row=0, column=0, padx=40)
        champPrenom.grid(row=0, column=1)
        frameJoueur.grid(row=1+i, column=0, sticky="n", padx = 10, pady = 10)
        entriesJoueurs.append(champPrenom)
    
    # Création du bouton
    frameBouton= Frame(fenetreMenu,background="#adff33")
    frameBouton.grid(row=7, column=0, sticky="n", padx = 10, pady = 10)
    bA = Button(frameBouton, text ='Ajouter', command = validerNom)
    bA.grid(row=0,column=0)         #.pack(side =LEFT, padx =3, pady =3)

    bRejouer = Button(frameBouton, text ='Rejouer', bg="#43c2df", fg="black", font=("Courier New", 11), command = rejouer) # !!! ne fonctionne pas
    bRejouer.grid(row=1,column=0,sticky="n", padx = 10, pady = 10) 

    btImageSon=PhotoImage(file="img/son.png")
    #bSon = Button(frameBouton, text="Son", bg="#43c2df", fg="black", font=("Courier New", 11), command=lambda: son())
    bSon = Button(frameBouton, image=btImageSon, command=son)
    bSon.grid(row=2,column=0,sticky="n", padx = 10, pady = 10) 
    bSon.image = btImageSon

    bCouperSon = Button(frameBouton, text="Couper son", bg="#43c2df", fg="black", font=("Courier New", 11), command=stop_son)
    bCouperSon.grid(row=2,column=1,sticky="n", padx = 10, pady = 10) 
    

    return variableJeu

    

def traitement_liste(liste):
    print("Liste reçue :", liste)

#popupMenu(traitement_liste)

#variableJeu=popupMenu(variableJeu)
#print(variableJeu["listeNomJoueur"])




def go(event,variableJeu):
    '''global decalage
    global nouvCarte
    #global x
    #global y
    global joueur
    global etat'''
    x=event.x #donnera la valeur de x
    y=event.y # donnera la valeur de y
    #print("fyeg",variableJeu["listeNomJoueur"])
    variableJeu["position"]= (x,y)                              # Tuple avec les coordonnées du clic
    
    if variableJeu["etat"]=='start':
        #instructionRetournerCarteDebutJn(variableJeu)
        variableJeu=retournerCarteDebut (x,y,variableJeu)

    
        
    else:
        instructionJeuJn(variableJeu)
        variableJeu =deroulerJeu(variableJeu)
        print (f"etat dans interface {variableJeu["etat"]}")

        if variableJeu["etat"]=='attente_pop-up' and variableJeu["typeJeu"]=="pioche":
            variableJeu=popupChoix(variableJeu)

        if variableJeu["etat"]=='changement_carte':
            print(x,y)
            print(len(images))
            xcoin,ycoin= recupCoordonnéeCarte(x,y,variableJeu["decalage"][(variableJeu["joueur"]-1)%4][0],variableJeu["decalage"][(variableJeu["joueur"]-1)%4][1])
            affichageCarteVerso(variableJeu["nouvCarte"],xcoin,ycoin)
            instructionJeuJn(variableJeu)
            affichagepioche(variableJeu["defausse"][0])
            variableJeu["etat"] ='choix_pioche'
        
        if variableJeu["etat"]== 'sup_colonne':

            affichageColonneSup(variableJeu)
            affichagepioche(variableJeu["defausse"][0])
            variableJeu["etat"]='choix_pioche'

        if verifFinJeu(variableJeu["joueur"]-1,variableJeu["listeEtatCarte"][variableJeu["joueur"]-1]) and not variableJeu["jeuTermine"]:
            variableJeu["dernierJoueur"] = variableJeu["joueur"]-1
            variableJeu["jeuTermine"]=TRUE

        if variableJeu["joueur"]== variableJeu["dernierJoueur"]:
            classement,score =chercheClassement(variableJeu)
            frameJeu.pack_forget()
            fenetreScore(str(classement[0]+1),score[classement[0]], str(classement[1]+1),score[classement[1]], str(classement[2]+1),score[classement[2]],str(classement[3]+1),score[classement[3]])
            frameScore.pack(fill="both", expand=True)            # afficher pop up
            
        '''if variableJeu["typeJeu"]=="defausse" :
            instructionPlacerCarteJn(variableJeu) 
            affichagepioche(variableJeu["defausse"][0])
            variableJeu["etat"]='changement_carte'  '''
        

    #print (etat)


'''variableJeu={
    "etat": "start",                                # Donne dans quel etat est le jeu (start,choix_pioche,choix_carte,changement_carte)
    "decalage": [[0,0],[980,0],[980,360],[0,360]]   # décalage des coordonnées des positions des jeux en fonction du joueur
    }
affichagecarteJnRecto(variableJeu)
affichagepioche()'''






''' Boutons ----------------------------------------------------------------------------------------'''

bQuitter = Button(frameJeu, text ='Quitter', bg="#43c2df", fg="black",font=("Courier New", 11), command = fenetrePrincipale.destroy)
bQuitter.place(anchor="se", x=530, y=690)

bMenu = Button(frameJeu, text ='Menu', bg="#43c2df", fg="black",font=("Courier New", 11), command = retournerAuMenu)
bMenu.place(anchor="sw", x=750, y=690)

btest = Button(frameJeu, text ='Test', bg="#43c2df", fg="black",font=("Courier New", 11), command = test)
btest.place(anchor="sw", x=650, y=690)
fenetreScore('vainqueur', 22, 'deuxieme', 24, 'troisieme', 33, 'quatrieme', 55)


bValider = Button(frameMenu, text = "Valider", width=10, height=1, command=valider)
bVider = Button(frameMenu, text = "Vider", width=10, height=1, command=vider)
bQuitter = Button(frameMenu, text = "Quitter", width=10, height=1, command=fenetrePrincipale.destroy)



''' Paramètres fonctions instructions joueurs --------------------------------------------------------------------------------------------------------------------------'''


# définir les Labels

# communs
nomJoueur = Label(frameJeu, font = "Selestin 18", fg = 'white', bg = 'black')
flecheDroite = Label(frameJeu, text = "==>", font = "Selestin 15", fg = 'white', bg = 'black')
flecheGauche = Label(frameJeu, text = "<==", font = "Selestin 15", fg = 'white', bg = 'black')

# instructionJeuJn
instruction_option = Label(frameJeu, text = "Vos options :", font = "Selestin 15", fg = 'white', bg = 'black')
instruction_piocherCarte = Label(frameJeu, text = "Piocher une carte \nPrendre une carte de la défausse \nRetourner une carte de votre jeu", font = "Selestin 15", fg = 'white', bg = 'black')

# instructionPlacerCarteJn
instruction_PlacerCarte = Label(frameJeu, text = "Placer la carte sur votre jeu", font = "Selestin 15", fg = 'white', bg = 'black')

# instructionChoisirEmplacementCarteJn
instruction_ChoixCarteRetourner = Label(frameJeu, text = "Choisir quelle carte vous voulez retourner", font = "Selestin 15", fg = 'white', bg = 'black')

# instructionRetournerCarteDebutJn
instructionRetourner2Carte = Label(frameJeu, text = "Veuillez retourner 2 cartes de votre jeu", font = "Selestin 15", fg = 'white', bg = 'black')







''' Paramètres fenêtre menu ---------------------------------------------------------------------------------------------'''

titre = Label(frameMenu, text="Menu Principal", font="Selestin 20", background="#1BB5E4", fg='black')

blanc = Label(frameMenu, text="", font="Selestin 20 bold", background="#1BB5E4")


# phrase pour dire d'écrire son nom 

nomJ1 = Label(frameMenu, text="Joueur 1, votre nom : ", font="Selestin 15", background="#1BB5E4", height=2, fg='black')
nomJ2 = Label(frameMenu, text="Joueur 2, votre nom : ", font="Selestin 15", background="#1BB5E4", height=2, fg='black')
nomJ3 = Label(frameMenu, text="Joueur 3, votre nom : ", font="Selestin 15", background="#1BB5E4", height=2, fg='black')
nomJ4 = Label(frameMenu, text="Joueur 4, votre nom : ", font="Selestin 15", background="#1BB5E4", height=2, fg='black')


# cadres pour écrire les noms 

cadreNomJ1 = Entry(frameMenu,  font="Selestin 15", justify = LEFT, fg='black')
cadreNomJ2 = Entry(frameMenu,  font="Selestin 15", justify = LEFT, fg='black')
cadreNomJ3 = Entry(frameMenu,  font="Selestin 15", justify = LEFT, fg='black')
cadreNomJ4 = Entry(frameMenu,  font="Selestin 15", justify = LEFT, fg='black')  

labListe = Label(frameMenu, text="Combien de joueurs êtes-vous ?", font="Selestin 15", background="#1BB5E4", height=2, fg='black')




''' Lancement des fonctions ------------------------------------------------------------------------------------------------------------------------'''

variableJeu=actionStart()
instructionRetournerCarteDebutJn(variableJeu)


fenetreMenu(variableJeu)
frameMenu.pack(fill='both', expand=True)






can.bind('<Button-1>', lambda event: go(event, variableJeu))



''' Ouverture de la fenêtre ------------------------------------------------------------------------------------------'''



fenetrePrincipale.mainloop()