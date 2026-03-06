from tkinter import *



fenetre = Tk()
fenetre.title("TP3 - Le morpion")

"""
largeur = fenetre.winfo_screenwidth()
hauteur = fenetre.winfo_screenheight()
fenetre.geometry(f"{largeur}x{hauteur}")
 
# Canvas principal
canvas = tk.Canvas(fenetre, bg="white")
canvas.pack(fill="both", expand=True)
#fill="both" : prend largeur + hauteur
#expand=True : utilise tout l’espace disponible
"""

can = Canvas(fenetre, width =1200, height =600, bg ='ivory')
can.pack(side =TOP, padx =0, pady =0)


bQ = Button(fenetre, text ='Quitter', command = fenetre.destroy)
bQ.pack(side =RIGHT, padx =3, pady =3)

bR= Button(fenetre, text ='Rejouer')
bR.pack(side =LEFT, padx =3, pady =3)


#grille()
#case = can.bind('<Button-1>', dessiner)















fenetre.mainloop()
