from tkinter import *
from jeu import *
from skyjo import *


# Fichier Interface Graphique du jeu - projet S4 informatique

''' Création de la fenêtre ----------------------------------------------------------------------------------------'''

fenetre = Tk()
fenetre.title("Skyjo")
fenetre.iconbitmap("eseoLogo.ico")

largeur = fenetre.winfo_screenwidth()
hauteur = fenetre.winfo_screenheight()

# la fenêtre prend tout l'écran
fenetre.geometry(f"{largeur}x{hauteur}+0+0")


"""
largeur = fenetre.winfo_screenwidth()
hauteur = fenetre.winfo_screenheight()
fenetre.geometry(f"{largeur}x{hauteur}")

# Canvas principal
canvas = tk.Canvas(fenetre, bg="white")
canvas.pack(fill="both", expand=True)
fill="both" : prend largeur + hauteur
expand=True : utilise tout l’espace disponible
"""

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



can = Canvas(fenetre, bg ='black')
can.place(anchor="nw", width=fenetre.winfo_screenwidth(), height=745, x=0, y=0)
    
'''
# cartes J1 (haut gauche)
can.create_rectangle(30, 10, 105, 115,width=1,fill="#808080") 
can.create_rectangle(30, 120, 105, 225,width=1,fill="#808080") 
can.create_rectangle(30, 230, 105, 335,width=1,fill="#808080") 

can.create_rectangle(110, 10, 185, 115,width=1,fill="#808080") 
can.create_rectangle(110, 120, 185, 225,width=1,fill="#808080") 
can.create_rectangle(110, 230, 185, 335,width=1,fill="#808080") 

can.create_rectangle(190, 10, 265, 115,width=1,fill="#808080") 
can.create_rectangle(190, 120, 265, 225,width=1,fill="#808080") 
can.create_rectangle(190, 230, 265, 335,width=1,fill="#808080") 

can.create_rectangle(270, 10, 345, 115,width=1,fill="#808080") 
can.create_rectangle(270, 120, 345, 225,width=1,fill="#808080") 
can.create_rectangle(270, 230, 345, 335,width=1,fill="#808080") 


# cartes J2 (haut droite)
can.create_rectangle(1010, 10, 1085, 115,width=1,fill="#808080") 
can.create_rectangle(1010, 120, 1085, 225,width=1,fill="#808080") 
can.create_rectangle(1010, 230, 1085, 335,width=1,fill="#808080") 

can.create_rectangle(1090, 10, 1165, 115,width=1,fill="#808080") 
can.create_rectangle(1090, 120, 1165, 225,width=1,fill="#808080") 
can.create_rectangle(1090, 230, 1165, 335,width=1,fill="#808080") 

can.create_rectangle(1170, 10, 1245, 115,width=1,fill="#808080") 
can.create_rectangle(1170, 120, 1245, 225,width=1,fill="#808080") 
can.create_rectangle(1170, 230, 1245, 335,width=1,fill="#808080") 

can.create_rectangle(1250, 10, 1325, 115,width=1,fill="#808080") 
can.create_rectangle(1250, 120, 1325, 225,width=1,fill="#808080") 
can.create_rectangle(1250, 230, 1325, 335,width=1,fill="#808080") 


# cartes J3 (bas droite)
can.create_rectangle(1010, 370, 1085, 475,width=1,fill="#808080") 
can.create_rectangle(1010, 480, 1085, 585,width=1,fill="#808080") 
can.create_rectangle(1010, 590, 1085, 695,width=1,fill="#808080") 

can.create_rectangle(1090, 370, 1165, 475,width=1,fill="#808080") 
can.create_rectangle(1090, 480, 1165, 585,width=1,fill="#808080") 
can.create_rectangle(1090, 590, 1165, 695,width=1,fill="#808080") 

can.create_rectangle(1170, 370, 1245, 475,width=1,fill="#808080") 
can.create_rectangle(1170, 480, 1245, 585,width=1,fill="#808080") 
can.create_rectangle(1170, 590, 1245, 695,width=1,fill="#808080") 

can.create_rectangle(1250, 370, 1325, 475,width=1,fill="#808080") 
can.create_rectangle(1250, 480, 1325, 585,width=1,fill="#808080") 
can.create_rectangle(1250, 590, 1325, 695,width=1,fill="#808080") 


# cartes J4 (bas gauche)
can.create_rectangle(30, 370, 105, 475,width=1,fill="#808080") 
can.create_rectangle(30, 480, 105, 585,width=1,fill="#808080") 
can.create_rectangle(30, 590, 105, 695,width=1,fill="#808080") 

can.create_rectangle(110, 370, 185, 475,width=1,fill="#808080") 
can.create_rectangle(110, 480, 185, 585,width=1,fill="#808080") 
can.create_rectangle(110, 590, 185, 695,width=1,fill="#808080") 

can.create_rectangle(190, 370, 265, 475,width=1,fill="#808080") 
can.create_rectangle(190, 480, 265, 585,width=1,fill="#808080") 
can.create_rectangle(190, 590, 265, 695,width=1,fill="#808080") 

can.create_rectangle(270, 370, 345, 475,width=1,fill="#808080") 
can.create_rectangle(270, 480, 345, 585,width=1,fill="#808080") 
can.create_rectangle(270, 590, 345, 695,width=1,fill="#808080") 

# Cartes de pioche et défausse 
can.create_rectangle(693, 315, 768, 420,width=1,fill="#808080")     #Défausse
can.create_rectangle(598, 315, 673, 420,width=1,fill="#808080")     #Pioche '''


''' Cartes -------------------------------------------------------------------------------------------------'''

'''J1=(0,0)
J2=(980,0)
J3=(980,360)
J4=(0,360)'''
images=[]
imagesPopUp=[]

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


def affichageCarteVerso (carte,x,y):
    global images
    listeImgCarteVerso=["img/-2.png","img/-1.png","img/0.png","img/1.png","img/2.png","img/3.png","img/4.png","img/5.png","img/6.png","img/7.png","img/8.png","img/9.png","img/10.png","img/11.png","img/12.png"]
    carte = PhotoImage(file=listeImgCarteVerso[carte+2])
    can.create_image(x+75/2, y+105/2, image=carte)      #can.create_image(x+a+75/2, y+b+105/2, image=carte)
    images.append(carte)
    
    

'''affichagecarteJnRecto(J1[0],J1[1])
affichagecarteJnRecto(J2[0],J2[1])
affichagecarteJnRecto(J3[0],J3[1])
affichagecarteJnRecto(J4[0],J4[1])'''


#affichageCarteVerso(2,30,10,J1[0],J1[1])




''' Affichage joueur et instructions -----------------------------------------------------------------------------------------'''



def instructionJeuJn(variableJeu) :

    # variableJeu["joueur"] = (de 0 à 3 : +1 pour le vrai numéro)

    numeroJn = variableJeu["joueur"] + 1
    nomJoueur = Label(fenetre, text = "C'est au joueur " + str(numeroJn) + " de jouer", font = "Selestin 18", fg = 'white', bg = 'black')
    instructions1 = Label(fenetre, text = "Vos options :", font = "Selestin 15", fg = 'white', bg = 'black')
    instructions2 = Label(fenetre, text = "Piocher une carte \nPrendre une carte de la défausse", font = "Selestin 15", fg = 'white', bg = 'black')
    instructions3 = Label(fenetre, text = "Quand vous avez fini, veuillez cliquer n'importe où sur la zone noire", font = "Selestin 15", fg = 'white', bg = 'black')
    flecheDroite = Label(fenetre, text = "==>", font = "Selestin 15", fg = 'white', bg = 'black')
    flecheGauche = Label(fenetre, text = "<==", font = "Selestin 15", fg = 'white', bg = 'black')
    # placer les phrases sur l'écran
    # texte.delete("1.0", "end")

    nomJoueur.place(anchor="center", x = 680, y = 60)
    instructions1.place(anchor="center", x = 680, y = 150)
    instructions2.place(anchor="center", x = 680, y = 220)
    instructions3.place(anchor="center", x = 680, y = 600)

    if numeroJn == 1 :
        flecheGauche.place(anchor="w", x = 350, y = 175)
    elif numeroJn == 2 :
        flecheDroite.place(anchor="e", x = 1000, y = 175)
    elif numeroJn == 3 :
        flecheDroite.place(anchor="e", x = 1000, y = 530)
    else :
        flecheGauche.place(anchor="w", x = 350, y = 530)




def instructionPlacerCarteJn(variableJeu) :

    # variableJeu["joueur"] = (de 0 à 3 : +1 pour le vrai numéro)

    numeroJn = variableJeu["joueur"] + 1
    nomJoueur = Label(fenetre, text = "C'est au joueur " + str(numeroJn) + " de jouer", font = "Selestin 18", fg = 'white', bg = 'black')
    instructions1 = Label(fenetre, text = "Placer la carte sur votre jeu", font = "Selestin 15", fg = 'white', bg = 'black')

    # placer les phrases sur l'écran

    nomJoueur.place(anchor="center", x = 680, y = 60)
    instructions1.place(anchor="center", x = 680, y = 150)



def instructionChoisirEmplacementCarteJn(variableJeu) :

    # variableJeu["joueur"] = (de 0 à 3 : +1 pour le vrai numéro)

    numeroJn = variableJeu["joueur"] + 1
    nomJoueur = Label(fenetre, text = "C'est au joueur " + str(numeroJn) + " de jouer", font = "Selestin 18", fg = 'white', bg = 'black')
    instructions1 = Label(fenetre, text = "Choisir quelle carte vous voulez retourner", font = "Selestin 15", fg = 'white', bg = 'black')

    # placer les phrases sur l'écran

    nomJoueur.place(anchor="center", x = 680, y = 60)
    instructions1.place(anchor="center", x = 680, y = 150)




def instructionPiocheDebutJn(variableJeu) :
    
    # affiche quel joueur piocher 2 cartes (seulement en début de partie)

    numeroJn = variableJeu["joueur"] + 1
    nomJoueur = Label(fenetre, text = "Joueur " + str(numeroJn), font = "Selestin 18", fg = 'white', bg = 'black')
    instruction1 = Label(fenetre, text = "Veuillez retourner 2 cartes de votre jeu", font = "Selestin 15", fg = 'white', bg = 'black')
    instruction2 = Label(fenetre, text = "Quand vous avez fini, veuillez cliquer n'importe où sur la zone noire", font = "Selestin 15", fg = 'white', bg = 'black')
    flecheDroite = Label(fenetre, text = "==>", font = "Selestin 15", fg = 'white', bg = 'black')
    flecheGauche = Label(fenetre, text = "<==", font = "Selestin 15", fg = 'white', bg = 'black')

    # placer les phrases sur l'écran

    nomJoueur.place(anchor="center", x = 680, y = 130)
    instruction1.place(anchor="center", x = 680, y = 180)
    instruction2.place(anchor="center", x = 680, y = 600)

    if numeroJn == 1 :
        flecheGauche.place(anchor="w", x = 350, y = 175)
    elif numeroJn == 2 :
        flecheDroite.place(anchor="e", x = 1000, y = 175)
    elif numeroJn == 3 :
        flecheDroite.place(anchor="e", x = 1000, y = 530)
    else :
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

    if variableJeu["nbCarteRetourner"]==2*variableJeu["nbJoueur"]:
        joueurDebut=variableJeu["sommeCarteRetourne"].index(max(variableJeu["sommeCarteRetourne"]))
        variableJeu["joueur"]=joueurDebut
        variableJeu["etat"]='choix_pioche'





''' Boutons Quitter/Rejouer ----------------------------------------------------------------------------------------'''
#Fonction pour remettre le jeu a zero
def rejouer ():
    etat ='start'


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


def popupScore(vainqueur, sVainqueur, deuxieme, sDeuxieme, troisieme=0, sTroisieme=0, quatrieme=0, sQuatrieme=0) :
    
    fenetreFin = Toplevel()
    fenetreFin.iconbitmap("eseoLogo.ico")
    fenetreFin.config(background='white')
    fenetreFin.title('Fin de la partie')
    fenetreFin.geometry("525x250+420+270") # dimensions et position de la fenêtre

    # messages    
    messageBravo = "Bravo ! " 
    messageVainqueur = vainqueur + " a gagné cette partie avec un score de " + str(sVainqueur) + " points"
    message2e = deuxieme + " a fini avec " + str(sDeuxieme) + " points"
    
    if troisieme != 0 : # il y a un troisième joueur
        message3e = troisieme + " a fini avec " + str(sTroisieme) + " points"
    
    if quatrieme != 0 : # il y a un quatrième joueur
        message4e = quatrieme + " a fini avec " + str(sQuatrieme) + " points"
    
    message1 = Label(fenetreFin, text=messageBravo, fg="blue", bg="white", font='Selestin 15')
    message2 = Label(fenetreFin, text=messageVainqueur, fg="blue", bg="white", font='Selestin 15')
    message3 = Label(fenetreFin, text=message2e, fg="blue", bg="white", font='Selestin 13')
    
    if troisieme != 0 : 
        message4 = Label(fenetreFin, text=message3e, fg="blue", bg="white", font='Selestin 13')
    
    if quatrieme != 0 :
        message5 = Label(fenetreFin, text=message4e, fg="blue", bg="white", font='Selestin 13')

    # placer sur l'écran
    message1.grid(row=1, column=0, sticky="n", padx = 10, pady = 10)
    message2.grid(row=2, column=0, sticky="n", padx = 10, pady = 10)
    message3.grid(row=4, column=0, sticky="n", padx = 10, pady = 10)
    
    if troisieme != 0 : 
        message4.grid(row=5, column=0, sticky="n", padx = 10, pady = 10)
    
    if quatrieme != 0 :
        message5.grid(row=6, column=0, sticky="n", padx = 10, pady = 10)






def go(event,variableJeu):
    '''global decalage
    global nouvCarte
    #global x
    #global y
    global joueur
    global etat'''
    x=event.x #donnera la valeur de x
    y=event.y # donnera la valeur de y

    variableJeu["position"]= (x,y)                              # Tuple avec les coordonnées du clic
    
    if variableJeu["etat"]=='start':
        instructionPiocheDebutJn(variableJeu)
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
            affichagepioche(variableJeu["defausse"][0])
            variableJeu["etat"] ='choix_pioche'
            
    

    #print (etat)


'''variableJeu={
    "etat": "start",                                # Donne dans quel etat est le jeu (start,choix_pioche,choix_carte,changement_carte)
    "decalage": [[0,0],[980,0],[980,360],[0,360]]   # décalage des coordonnées des positions des jeux en fonction du joueur
    }
affichagecarteJnRecto(variableJeu)
affichagepioche()'''

variableJeu=actionStart()


#can.pack(fill="both",expand=YES)


''' Boutons Quitter/Rejouer ----------------------------------------------------------------------------------------'''

bQuitter = Button(fenetre, text ='Quitter', command = fenetre.destroy)
bQuitter.place(anchor="se", x=405, y=690)

bRejouer= Button(fenetre, text ='Rejouer', command= rejouer)
bRejouer.place(anchor="sw", x=948, y=690)






can.bind('<Button-1>', lambda event: go(event, variableJeu))





fenetre.mainloop()
