from tkinter import *
from tkinter.messagebox import *
from bouton import *
from sac import *
from joueur import Joueur
from playsound import playsound
import sql_methode
import sqlite3

def main_menu(id, joueur, n=False):

    if not n:
        intro()
    else:

        introtk = Tk()
        introtk.title("Pokémon Orange Garnet")
        introtk.resizable(width=False, height=False)

        image = PhotoImage(master = introtk, file = "bg\intro.png")
        Label(introtk, image = image).pack()

        introtk.after(7000, lambda: introtk.destroy())

        introtk.mainloop()

    menu_general = Tk()
    menu_general.title("Pokémon Orange Garnet")
    menu_general.geometry('768x640')
    menu_general.resizable(width=False, height=False)

    image = PhotoImage(master = menu_general, file = "bg\menu_principal.png")
    Label(menu_general, image = image).place(x=0, y=0)

    menubar = Menu(menu_general)

    menu1 = Menu(menu_general, tearoff=0)
    menu1.add_command(label = "Carte Joueur", command = lambda : carte_joueur(id))
    menu1.add_separator()
    menu1.add_command(label = "Equipe", command = lambda : equipeA(id, joueur.get_equipe(), joueur))
    menu1.add_command(label = "PC", command = lambda : pcA(id, joueur.get_pc(), joueur))
    menubar.add_cascade(label = "Information", menu = menu1)

    items = sql_methode.get_nbr_items(id)
    menu2 = Menu(menu_general, tearoff = 0)
    menu2.add_command(label = "Pokeball : {}".format(items["pokeball"]), state = DISABLED)
    menu2.add_command(label = "Superball : {}".format(items["superball"]), state = DISABLED)
    menu2.add_command(label = "Hyperball : {}".format(items["hyperball"]), state = DISABLED)
    menu2.add_command(label = "Potion : {}".format(items["potion"]), state = DISABLED)
    menu2.add_command(label = "Super Potion : {}".format(items["superpotion"]), state = DISABLED)
    menu2.add_command(label = "Hyper Potion : {}".format(items["hyperpotion"]), state = DISABLED)
    menu2.add_command(label = "Potion Max : {}".format(items["potionmax"]), state = DISABLED)
    menubar.add_cascade(label = "Sac", menu = menu2)

    inf_joueur = sql_methode.info_joueur(id)
    menu3 = Menu(menu_general, tearoff = 0)

    menubar.add_cascade(label = "Or", menu = menu3)
    menu3.add_command(label = "{}".format(inf_joueur[6]), state = DISABLED)
    menu_general.config(menu=menubar)

    creation_button(menu_general, joueur)

    #menu_general.protocol("WM_DELETE_WINDOW", lambda : close_game(menu_general))
    menu_general.mainloop()

def starter(id, mdp, pseudo):

    new_player()

    prof = Tk()
    prof.title("Professeur Maimone")
    prof.resizable(width=False, height=False)


    Label(prof, text = "TADA! Voici la suprise que j'ai préparé spécialement pour toi, 26 Pokémons rares!\n"+
                            "Tu t'en doutes ahah, mais oui! tu vas pouvoir choisir parmi l'un d'entre eux, ne suis-je pas généreux!\n"+
                                "Il te suffit de cliquer sur celui que tu veux et il deviendra ton compagnon à vie!", font = ('Arial', 10)).pack(pady=10)
    image = PhotoImage(master = prof, file = "bg\professeur_maimonec.png")
    Label(prof, image = image).pack()



    starter = Tk()
    starter.title("Starter")
    starter.geometry("1080x640")
    starter.resizable(width=False, height=False)

    sprites = sql_methode.sprites(starter)

    Button(starter, image = sprites[1], command = lambda: valide(starter, prof, id, mdp, pseudo, 1)).place(x = 108, y = 214)
    Button(starter, image = sprites[4], command = lambda: valide(starter, prof, id, mdp, pseudo, 4)).place(x = 108, y = 321)
    Button(starter, image = sprites[7], command = lambda: valide(starter, prof, id, mdp, pseudo, 7)).place(x = 108, y = 428)
    Button(starter, image = sprites[25], command = lambda: valide(starter, prof, id, mdp, pseudo, 25)).place(x = 270, y = 107)
    Button(starter, image = sprites[133], command = lambda: valide(starter, prof, id, mdp, pseudo, 133)).place(x = 675, y = 107)
    Button(starter, image = sprites[152], command = lambda: valide(starter, prof, id, mdp, pseudo, 152)).place(x = 216, y = 214)
    Button(starter, image = sprites[155], command = lambda: valide(starter, prof, id, mdp, pseudo, 155)).place(x = 216, y = 321)
    Button(starter, image = sprites[158], command = lambda: valide(starter, prof, id, mdp, pseudo, 158)).place(x = 216, y = 428)
    Button(starter, image = sprites[252], command = lambda: valide(starter, prof, id, mdp, pseudo, 252)).place(x = 324, y = 214)
    Button(starter, image = sprites[255], command = lambda: valide(starter, prof, id, mdp, pseudo, 255)).place(x = 324, y = 321)
    Button(starter, image = sprites[258], command = lambda: valide(starter, prof, id, mdp, pseudo, 258)).place(x = 324, y = 428)
    Button(starter, image = sprites[387], command = lambda: valide(starter, prof, id, mdp, pseudo, 387)).place(x = 432, y = 214)
    Button(starter, image = sprites[390], command = lambda: valide(starter, prof, id, mdp, pseudo, 390)).place(x = 432, y = 321)
    Button(starter, image = sprites[393], command = lambda: valide(starter, prof, id, mdp, pseudo, 393)).place(x = 432, y = 428)
    Button(starter, image = sprites[495], command = lambda: valide(starter, prof, id, mdp, pseudo, 495)).place(x = 540, y = 214)
    Button(starter, image = sprites[498], command = lambda: valide(starter, prof, id, mdp, pseudo, 498)).place(x = 540, y = 321)
    Button(starter, image = sprites[501], command = lambda: valide(starter, prof, id, mdp, pseudo, 501)).place(x = 540, y = 428)
    Button(starter, image = sprites[650], command = lambda: valide(starter, prof, id, mdp, pseudo, 650)).place(x = 648, y = 214)
    Button(starter, image = sprites[653], command = lambda: valide(starter, prof, id, mdp, pseudo, 653)).place(x = 648, y = 321)
    Button(starter, image = sprites[656], command = lambda: valide(starter, prof, id, mdp, pseudo, 656)).place(x = 648, y = 428)
    Button(starter, image = sprites[722], command = lambda: valide(starter, prof, id, mdp, pseudo, 722)).place(x = 756, y = 214)
    Button(starter, image = sprites[725], command = lambda: valide(starter, prof, id, mdp, pseudo, 725)).place(x = 756, y = 321)
    Button(starter, image = sprites[728], command = lambda: valide(starter, prof, id, mdp, pseudo, 728)).place(x = 756, y = 428)
    Button(starter, image = sprites[810], command = lambda: valide(starter, prof, id, mdp, pseudo, 810)).place(x = 864, y = 214)
    Button(starter, image = sprites[813], command = lambda: valide(starter, prof, id, mdp, pseudo, 813)).place(x = 864, y = 321)
    Button(starter, image = sprites[816], command = lambda: valide(starter, prof, id, mdp, pseudo, 816)).place(x = 864, y = 428)

    prof.mainloop()
    starter.mainloop()

def valide(fenetre1, fenetre2, id, mdp, pseudo, idpokemon):

    fenetre1.destroy()
    fenetre2.destroy()

    prof = Tk()
    prof.title("Professeur Maimone")
    prof.resizable(width=False, height=False)


    Label(prof, text="Mais avant que ton aventure ne commence vraiment, laisse moi t'en dire plus sur ce monde.\n"+
                        "Ne t'enerve pas, je suis sûr que tu ne connais même pas le nom de ce pays!\n"+
                            "Tu te trouves à Kyydem.", font = ('Arial', 10)).pack(pady=10)
    image = PhotoImage(master = prof, file = "bg\professeur_maimonec.png")
    Label(prof, image = image).pack()

    prof.after(10000, lambda:prof.destroy())
    prof.mainloop()


    prof = Tk()
    prof.title("Professeur Maimone")
    prof.resizable(width=False, height=False)


    Label(prof, text="Non en vrai on s'en fou!, tu n'as rien à savoir!\n"+
                        "Des méchants? même pas, et oui notre monde est tranquil.\n"+
                        "Le seul truc a faire c'est devenir le meilleur des dresseurs!", font = ('Arial', 10)).pack(pady=10)
    image = PhotoImage(master = prof, file = "bg\professeur_maimonec.png")
    Label(prof, image = image).pack()

    prof.after(10000, lambda:prof.destroy())
    prof.mainloop()


    prof = Tk()
    prof.title("Professeur Maimone")
    prof.resizable(width=False, height=False)


    Label(prof, text="Mais après peut-être qu'un jour quelque chose de special arrivera à ce monde !?", font = ('Arial', 10)).pack(pady=10)
    image = PhotoImage(master = prof, file = "bg\professeur_maimonec.png")
    Label(prof, image = image).pack()

    prof.after(2000, lambda:prof.destroy())
    prof.mainloop()


    sql_methode.update_golds(id, 5000)
    main_menu(id, Joueur(id, mdp, pseudo, new = [True, [5, idpokemon]]), n = True)

def intro():

    prof = Tk()
    prof.title("Professeur Maimone")
    prof.resizable(width=False, height=False)

    Label(prof, text="Oh! te revoilà parmi nous, prêt à continuer ton aventure pokemon?", font = ('Arial', 10)).pack(pady=10)
    image2 = PhotoImage(master = prof, file = "bg\professeur_maimonec.png")
    Label(prof, image = image2).pack()

    intro = Tk()
    intro.title("Pokémon Orange Garnet")
    intro.resizable(width=False, height=False)

    image1 = PhotoImage(master = intro, file = "bg\intro.png")
    Label(intro, image = image1).pack()


    prof.after(4000, lambda: prof.destroy())
    intro.after(7000, lambda: intro.destroy())

    prof.mainloop()
    intro.mainloop()

def new_player():

    playsound('intro.mp3', block=False)

    prof = Tk()
    prof.title("Professeur Maimone")
    prof.resizable(width=False, height=False)


    Label(prof, text="Éh bien! Éh bien! Je me disais bien t'avoir déjà vu.\n"+
                        "Tu es le nouveau challenger de ce pays n'est-ce pas?", font = ('Arial', 10)).pack(pady=10)
    image = PhotoImage(master = prof, file = "bg\professeur_maimonec.png")
    Label(prof, image = image).pack()

    prof.after(10000, lambda:prof.destroy())
    prof.mainloop()


    prof = Tk()
    prof.title("Professeur Maimone")
    prof.resizable(width=False, height=False)

    Label(prof, text = "Oh! mais laisse moi me présenter!\nJe nomme Maimone, mais tout le monde m'appelle Professeur Pokémon."+
                                " Mais toi tu peux m'appeler ce so... hum,\nProfesseur Maimone ou M.Maimone comme tu le souhaites", font = ('Arial', 10)).pack(pady=10)
    image = PhotoImage(master = prof, file = "bg\professeur_maimonec.png")
    Label(prof, image = image).pack()

    prof.after(10000, lambda:prof.destroy())
    prof.mainloop()


    prof = Tk()
    prof.title("Professeur Maimone")
    prof.resizable(width=False, height=False)


    Label(prof, text = "M'enfin, si tu es là ce n'est pas pour savoir comment m'appeler, mais pour commencer ton histoire pas vrai?\n"+
                                    "Très bien, je vois que tu meurs d'impatience, alors arrêtons de tergiverser!", font = ('Arial', 10)).pack(pady=10)
    image = PhotoImage(master = prof, file = "bg\professeur_maimonec.png")
    Label(prof, image = image).pack()

    prof.after(10000, lambda:prof.destroy())
    prof.mainloop()


    prof = Tk()
    prof.title("Professeur Maimone")
    prof.resizable(width=False, height=False)

    Label(text = "Cependant..., tu ne peux pas partir comme cela, ce monde est rempli de pokémon sauvage et dangereux!\n"+
                                    "Ah mais ne t'en fais pas! j'ai pensé à tout REGARDE!", font = ('Arial', 10)).pack(pady=10)
    image = PhotoImage(master = prof, file = "bg\professeur_maimonec.png")
    Label(prof, image = image).pack()

    prof.after(10000, lambda:prof.destroy())
    prof.mainloop()


def close_game(menu_general):
    if askokcancel("Quit", "Voulez-vous quitter le monde des Pokémons ?"):
        menu_general.destroy()
        exit()

