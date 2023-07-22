from tkinter import *
import sql_methode
import sqlite3


def carte_joueur(id):


    info = sql_methode.info_joueur(id)

    if info[3] > 0:
        win_rate = info[4]//info[3]*100
        loose_rate = 100-win_rate
    else:
        win_rate, loose_rate = 'None', 'None'

    carte_joueur = Tk()
    carte_joueur.title("Carte de {}".format(info[0]))
    carte_joueur.resizable(width=False, height=False)

    carte_joueur["padx"] = 73
    carte_joueur["pady"] = 73

    Label(carte_joueur, text = "Pseudo", font = ('Arial Black', 10)).pack()
    Label(carte_joueur, text = info[0], font = ('Arial', 10)).pack()

    """Label(carte_joueur, text = "Temps de jeux", font = ('Arial Black', 10)).pack()
    Label(carte_joueur, text = info[1], font = ('Arial', 10)).pack()"""

    Label(carte_joueur, text = "Nombre de connexion", font = ('Arial Black', 10)).pack()
    Label(carte_joueur, text = info[2], font = ('Arial', 10)).pack()

    Label(carte_joueur, text = "Nombre de combat", font = ('Arial Black', 10)).pack()
    Label(carte_joueur, text = info[3], font = ('Arial', 10)).pack()

    Label(carte_joueur, text = "Win rate", font = ('Arial Black', 10)).pack()
    Label(carte_joueur, text = str(win_rate), font = ('Arial', 10)).pack()

    Label(carte_joueur, text = "Loose rate", font = ('Arial Black', 10)).pack()
    Label(carte_joueur, text = str(loose_rate), font = ('Arial', 10)).pack()

    Label(carte_joueur, text = "Golds", font = ('Arial Black', 10)).pack()
    Label(carte_joueur, text = info[6], font = ('Arial', 10)).pack()

    carte_joueur.mainloop()

def equipeA(id, equipe_id, joueur):

    global joueurObjet, equipe
    joueurObjet = joueur

    equipe = Tk()
    equipe.title("Équipe")
    equipe.resizable(width=False, height=False)

    equipe["padx"] = 120
    equipe["pady"] = 20

    sprites = sql_methode.sprites(equipe)
    n_equipe_id = sql_methode.get_id_pokemon(equipe_id)

    for i in n_equipe_id:

        z = equipe_id[0]
        eval("Button(equipe, image = sprites[i[0]], command = lambda: info_poke("+str(z)+")).pack(pady = 10)")
        equipe_id = equipe_id[1:len(equipe_id)]


    equipe.mainloop()

def pcA(id, pc_id, joueur):

    global joueurObjet, pc
    joueurObjet = joueur

    pc = Tk()
    pc.title("PC")
    pc.geometry("1080x820")
    pc.resizable(width=False, height=False)

    sprites = sql_methode.sprites(pc)
    n_pc_id = sql_methode.get_id_pokemon(pc_id)

    x,y = 1080, 820
    x = x//(len(n_pc_id)+2)
    consx=x
    y = y//(len(n_pc_id)+1)
    consy=y
    for i in n_pc_id:

        z = pc_id[0]
        eval("Button(pc, image = sprites[i[0]], command = lambda: info_poke("+str(z)+")).place(x=consx, y=consy)")
        consx= consx+x+40
        pc_id = pc_id[1:len(pc_id)]

        if consx >= x * 20:
            consy = consy+y+35
            consx = x

    pc.mainloop()

def info_poke(id):

    global joueurObjet, equipe, pc

    info = Tk()
    info.title("Résumé")
    info.resizable(width=False, height=False)

    info["padx"] = 120
    info["pady"] = 20

    color = ["Black","Black","Black","Black","Black","Black"]
    can = sql_methode.cantine_get(id)
    if len(can) > 0:
        for i in range(6):
            if i == can[0][1]:
                color[i] = "Red"
            elif len(can) == 2:
                if i == can[1][1]:
                    color[i] = "Red"

    stats = sql_methode.get_stat_poke_joueur(id)

    Label(info, text = "Nom", font = ('Arial Black', 10)).pack()
    Label(info, text = stats["nom"], font = ('Arial', 10)).pack(pady = 10)

    Label(info, text = "Level", font = ('Arial Black', 10), fg = "Orange").pack()
    Label(info, text = stats["niveau"], font = ('Arial', 10)).pack(pady = 10)

    Label(info, text = "Hp", font = ('Arial Black', 10), fg = "Green").pack()
    Label(info, text = stats["hp"], font = ('Arial', 10), fg = color[0]).pack(pady = 10)

    Label(info, text = "Attaque", font = ('Arial Black', 10), fg = "Red").pack()
    Label(info, text = stats["atk"], font = ('Arial', 10), fg = color[1]).pack(pady = 10)

    Label(info, text = "Defense", font = ('Arial Black', 10), fg = "Blue").pack()
    Label(info, text = stats["def"], font = ('Arial', 10), fg = color[2]).pack(pady = 10)

    Label(info, text = "Attaque Spéciale", font = ('Arial Black', 10), fg = "Red").pack()
    Label(info, text = stats["sp_atk"], font = ('Arial', 10), fg = color[3]).pack(pady = 10)

    Label(info, text = "Défense Spéciale", font = ('Arial Black', 10), fg = "Blue").pack()
    Label(info, text = stats["sp_def"], font = ('Arial', 10), fg = color[4]).pack(pady = 10)

    Label(info, text = "Vitesse", font = ('Arial Black', 10), fg = "Pink").pack()
    Label(info, text = stats["spd"], font = ('Arial', 10), fg = color[5]).pack(pady = 10)

    Label(info, text = "Talent", font = ('Arial Black', 10), fg = "Orange").pack()
    Label(info, text = stats["talent"], font = ('Arial', 10)).pack(pady = 10)

    if stats["teampoke"] == "1":
        Button(info, text = "Envoyer au PC", command = lambda: joueurObjet.team_to_pc(id, info, equipe)).pack()
    elif stats["teampoke"] == "0":
        Button(info, text = "Amener dans l'équipe", command = lambda: joueurObjet.pc_to_team(id, info, pc)).pack()

    info.mainloop()

def warning(bool):

    if bool:
        prof = Tk()
        prof.title("Professeur Maimone")
        prof.resizable(width=False, height=False)


        Label(prof, text="Je t'interdis de déposer ton dernier pokémon au PC!\n"+
                            "Le monde est dangereux sans personne pour te protéger!", font = ('Arial', 10)).pack(pady=10)
        image = PhotoImage(master = prof, file = "bg\professeur_maimonec.png")
        Label(prof, image = image).pack()

        prof.after(4000, lambda:prof.destroy())
        prof.mainloop()
    else:
        prof = Tk()
        prof.title("Professeur Maimone")
        prof.resizable(width=False, height=False)


        Label(prof, text="Il faut savoir ne pas abuser des bonnes choses!\n"+
                            "Tu ne peux pas prendre plus de 6 pokémons dans ton équipe.", font = ('Arial', 10)).pack(pady=10)
        image = PhotoImage(master = prof, file = "bg\professeur_maimonec.png")
        Label(prof, image = image).pack()

        prof.after(4000, lambda:prof.destroy())
        prof.mainloop()