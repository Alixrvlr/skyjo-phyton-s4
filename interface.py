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

print(hauteur-60, fenetre.winfo_screenwidth())

# test taille joueur
can = Canvas(fenetre, bg ='black')
can.place(anchor="nw", width=550, height=290, x=0, y=0)







''' Boutons Quitter/Rejouer ----------------------------------------------------------------------------------------'''

bQuitter = Button(fenetre, text ='Quitter', command = fenetre.destroy)
#bQuitter.grid(row=35, column=0, sticky="s", padx = 5, pady = 1)

bRejouer= Button(fenetre, text ='Rejouer')
#bRejouer.grid(row=35, column=5, sticky="s", padx = 5, pady = 1)


#grille()
#case = can.bind('<Button-1>', dessiner)









fenetre.mainloop()
