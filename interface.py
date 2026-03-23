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


# test taille joueur
can = Canvas(fenetre, bg ='black')
can.place(anchor="nw", width=fenetre.winfo_screenwidth(), height=710, x=0, y=0)

# fonction emplacement des cartes d'un joueur
def emplacement_cartes_Jn(x0,y0) :
    # à terminer !!!!!!!
    can.create_rectangle(x0, y0, x0+75, y0+105,width=1,fill="#808080") 
    can.create_rectangle(x0, y0+110, 105, 225,width=1,fill="#808080") 
    can.create_rectangle(x0, 230, 105, 335,width=1,fill="#808080") 

    can.create_rectangle(110, 10, 185, 115,width=1,fill="#808080") 
    can.create_rectangle(110, 120, 185, 225,width=1,fill="#808080") 
    can.create_rectangle(110, 230, 185, 335,width=1,fill="#808080") 

    can.create_rectangle(190, 10, 265, 115,width=1,fill="#808080") 
    can.create_rectangle(190, 120, 265, 225,width=1,fill="#808080") 
    can.create_rectangle(190, 230, 265, 335,width=1,fill="#808080") 

    can.create_rectangle(270, 10, 345, 115,width=1,fill="#808080") 
    can.create_rectangle(270, 120, 345, 225,width=1,fill="#808080") 
    can.create_rectangle(270, 230, 345, 335,width=1,fill="#808080") 
    

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
can.create_rectangle(598, 315, 673, 420,width=1,fill="#808080")     #Pioche


''' Faces des cartes ---------------------------------------------------------------------------------------'''

J1=(0,0)
J2=(980,0)
J3=(980,360)
J4=(0,360)
images=[]
def affichagecarteJnRecto(a,b):
    versocarte=PhotoImage(file="img/verso.png")#.subsample(3)
    x=[30,30,30,110,110,110,190,190,190,270,270,270]
    y=[10,120,230,10,120,230,10,120,230,10,120,230]
    for i in range (12):
        can.create_image(x[i]+a+75/2,y[i]+b+105/2,image=versocarte)
    images.append(versocarte)


def affichageCarteVerso (carte,x,y,a,b):
    listeImgCarteVerso=["img/-2.png","img/-1.png","img/0.png","img/1.png","img/2.png","img/3.png","img/4.png","img/5.png","img/6.png","img/7.png","img/8.png","img/9.png","img/10.png","img/11.png","img/12.png"]
    test = PhotoImage(file=listeImgCarteVerso[carte+2])
    can.create_image(x+a+75/2,y+b+105/2,image=test)
    images.append(test)
    
    

affichagecarteJnRecto(J1[0],J1[1])
affichagecarteJnRecto(J2[0],J2[1])
affichagecarteJnRecto(J3[0],J3[1])
affichagecarteJnRecto(J4[0],J4[1])

#affichageCarteVerso(2,30,10,J1[0],J1[1])
can.pack(fill="both",expand=YES)


''' Boutons Quitter/Rejouer ----------------------------------------------------------------------------------------'''
#Fonction pour remettre le jeu a zero
def rejouer ():
    etat ='start'


bQuitter = Button(fenetre, text ='Quitter', command = fenetre.destroy)
bQuitter.place(anchor="se", x=80, y=730)

bRejouer= Button(fenetre, text ='Rejouer', command= rejouer)
bRejouer.place(anchor="sw", x=1275, y=730)


''' Fenêtre Pop-Up pour montrer la carte piochée -------------------------------------------------------------------'''
def popupChoix() :
    # fenêtre popup : à terminer !!!!
    messageChoix = "Voulez-vous jouer cette carte ?"
    miniFenetre = Toplevel()
    miniFenetre.iconbitmap("eseoLogo.ico")
    miniFenetre.config(background='white')
    miniFenetre.title('Choix')
    miniFenetre.geometry("280x340+550+200")
    message = Label(miniFenetre, text=messageChoix, fg="blue", bg="white", font='Selestin 15')

    # emplacement de la carte
    # largeur = 125
    # hauteur = 175
    carte = Canvas(miniFenetre, bg ='black',width=140, height=195)

    # boutons
    oui = Button(miniFenetre, text ='Oui')
    non = Button(miniFenetre, text ='Non')

    # placer les boutons
    message.grid(row=1, column=0, sticky="n", padx = 1, pady = 10)
    carte.grid(row=2, column=0, sticky="n", padx = 5, pady = 10)
    oui.grid(row=4, column=0, sticky="w", padx = 5, pady = 5)
    non.grid(row=4, column=0, sticky="e", padx = 5, pady = 5)

'''test popup'''
#popupChoix()



#case = can.bind('<Button-1>', dessiner)


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
    
    variableJeu =deroulerJeu(variableJeu)
    print (f"etat dans interface {variableJeu["etat"]}")
    if variableJeu["etat"]=='changement_carte':
        affichageCarteVerso(variableJeu["nouvCarte"],x,y,variableJeu["decalage"][variableJeu["joueur"]-2][0],variableJeu["decalage"][variableJeu["joueur"]-2][1])
        variableJeu["etat"] ='choix_pioche'
    

    #print (etat)


variableJeu={
    "etat": "start",                                # Donne dans quel etat est le jeu (start,choix_pioche,choix_carte,changement_carte)
    
    "decalage": [[0,0],[980,0],[980,360],[0,360]]   # décalage des coordonnées des positions des jeux en fonction du joueur
    }

can.bind('<Button-1>', lambda event: go(event, variableJeu))





fenetre.mainloop()
