from tkinter import *
from tkinter.messagebox import *
import sqlite3
from menu_principal import *
from joueur import Joueur

conn = sqlite3.connect('TablePokemon.db')

def main():
    cur = conn.cursor()
    req = "select Pseudo, Mdp from Joueur;"
    cur.execute(req)

    playerlist = cur.fetchall()
    conn.commit()
    cur.close()

    identification(playerlist)

def identification(playerlist):

    menu_connexion = Tk()
    menu_connexion.title("Connexion")
    menu_connexion.geometry('300x200')
    menu_connexion.resizable(width=False, height=False)

    pseudo_label = Label(menu_connexion, text = "Pseudo").pack(pady = 5)
    pseudo_entry = Entry(menu_connexion, width = 30)
    pseudo_entry.pack()

    mdp_label = Label(menu_connexion, text = "Mot De Passe").pack(pady = 5)
    mdp_entry = Entry(menu_connexion, width = 30, show = "*")
    mdp_entry.pack()

    bouton_valider = Button(menu_connexion, text = "Valider",
                   command = lambda: valider(menu_connexion, pseudo_entry.get(), mdp_entry.get(), playerlist))
    bouton_valider.pack(pady=10)

    bouton_inscription = Button(menu_connexion, text = "Inscrivez-vous",
                   command = lambda: inscription(menu_connexion, playerlist))
    bouton_inscription.pack(pady=10)


    menu_connexion.protocol("WM_DELETE_WINDOW", lambda : close_game(menu_connexion))
    menu_connexion.mainloop()

def valider(menu, pseudo, mdp, playerlist):

    if pseudo == "":
       showwarning("Impossible", "Vous devez entrer un pseudo d'une lettre au minimum")
    elif (pseudo, mdp) in playerlist:

         cur = conn.cursor()
         req = "select id from Joueur where (pseudo, mdp) = ('" + pseudo + "','" + mdp + "');"
         cur.execute(req)

         id = cur.fetchall()[0][0]

         req = "UPDATE Joueur SET NbrDeConnexion = NbrDeConnexion+1 where id = " + str(id)
         cur.execute(req)



         conn.commit()
         cur.close()
         conn.close()

         menu.destroy()
         main_menu(id, Joueur(id, mdp, pseudo))
    else:
         showwarning("Impossible", "Pseudo ou Mot de passe incorrect")

def inscription(menu, playerlist):

    menu.destroy()
    menu_inscription = Tk()
    menu_inscription.title("Inscription")
    menu_inscription.geometry('300x200')
    menu_inscription.resizable(width=False, height=False)

    pseudo_label = Label(menu_inscription, text = "Pseudo").pack(pady = 5)
    pseudo_entry = Entry(menu_inscription, width = 30)
    pseudo_entry.pack()

    mdp_label = Label(menu_inscription, text = "Mot De Passe").pack(pady = 5)
    mdp_entry = Entry(menu_inscription, width = 30, show = "*")
    mdp_entry.pack()

    bouton_valider = Button(menu_inscription, text = "Valider",
                   command = lambda: stock(pseudo_entry.get(), mdp_entry.get(), menu_inscription, playerlist))
    bouton_valider.pack(pady=10)

    bouton_retour = Button(menu_inscription, text = "Retour",
                   command = lambda: retour(menu_inscription, playerlist))
    bouton_retour.pack(pady=10)

    menu_inscription.protocol("WM_DELETE_WINDOW", lambda : close_game(menu_inscription))
    menu_inscription.mainloop()

def retour(menu_inscription, playerlist):
    menu_inscription.destroy()
    identification(playerlist)

def stock(pseudo, mdp, menu, playerlist):

    doublon = False
    for i in playerlist:
        if pseudo == i[0]:
            doublon = True

    if pseudo == "" or mdp == "":
       showwarning("Impossible", "Vous devez entrer un pseudo et un mot de passe")
    elif not doublon:

         cur = conn.cursor()
         req = "insert into Joueur ('Mdp', 'Pseudo')"
         req += " values ('" + mdp + "','" + pseudo + "');"

         cur.execute(req)

         req = "select id from Joueur where (pseudo, mdp) = ('" + pseudo + "','" + mdp + "');"
         cur.execute(req)

         id = cur.fetchall()[0][0]

         conn.commit()
         cur.close()
         conn.close()

         menu.destroy()

         starter(id, mdp, pseudo)
    else:
        showwarning("Impossible", "Un joueur possède déjà ce pseudo !")


##if __name__ == '__main__':
    main()

main()