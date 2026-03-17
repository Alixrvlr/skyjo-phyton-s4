from tkinter import *

# Fichier Interface Graphique du jeu - projet S4 informatique

''' Création de la fenêtre ----------------------------------------------------------------------------------------'''

fenetre = Tk()
fenetre.title("Skyjo")
fenetre.iconbitmap("logo.ico")

largeur = fenetre.winfo_screenwidth()
hauteur = fenetre.winfo_screenheight()

# la fenêtre prend tout l'écran
fenetre.geometry(f"{largeur}x{hauteur}")


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
# width=(largeur/2)-(largeur/10) = 550
# height=((hauteur-60)/2)-70 = 290

# Délimitation d'une carte 
# width = 75
# height = 290//3 = 105


# test taille joueur
can = Canvas(fenetre, bg ='black')
can.place(anchor="nw", width=fenetre.winfo_screenwidth(), height=710, x=0, y=0)

# cartes J1 (haut gauche)
can.create_rectangle(10, 10, 85, 115,width=1,fill="#808080") 
can.create_rectangle(10, 120, 85, 225,width=1,fill="#808080") 
can.create_rectangle(10, 230, 85, 335,width=1,fill="#808080") 

can.create_rectangle(90, 10, 165, 115,width=1,fill="#808080") 
can.create_rectangle(90, 120, 165, 225,width=1,fill="#808080") 
can.create_rectangle(90, 230, 165, 335,width=1,fill="#808080") 

can.create_rectangle(170, 10, 245, 115,width=1,fill="#808080") 
can.create_rectangle(170, 120, 245, 225,width=1,fill="#808080") 
can.create_rectangle(170, 230, 245, 335,width=1,fill="#808080") 

can.create_rectangle(250, 10, 325, 115,width=1,fill="#808080") 
can.create_rectangle(250, 120, 325, 225,width=1,fill="#808080") 
can.create_rectangle(250, 230, 325, 335,width=1,fill="#808080") 




''' Boutons Quitter/Rejouer ----------------------------------------------------------------------------------------'''

bQuitter = Button(fenetre, text ='Quitter', command = fenetre.destroy)
#bQuitter.grid(row=35, column=0, sticky="s", padx = 5, pady = 1)

bRejouer= Button(fenetre, text ='Rejouer')
#bRejouer.grid(row=35, column=5, sticky="s", padx = 5, pady = 1)


#grille()
#case = can.bind('<Button-1>', dessiner)









fenetre.mainloop()
