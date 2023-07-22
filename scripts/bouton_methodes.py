from tkinter import *
from tkinter.messagebox import *
from random import choice, randint
from time import sleep
import sql_methode


table_des_types_efficace = {
                            "Normal": [],
                            "Fighting": ["Normal", "Rock", "Steel", "Ice", "Dark"],
                            "Flying": ["Fighting", "Bug", "Grass"],
                            "Poison": ["Grass", "Fairy"],
                            "Ground": ["Poison", "Rock", "Steel", "Fire", "Electric"],
                            "Rock": ["Flying", "Bug", "Fire", "Ice"],
                            "Bug": ["Grass", "Psychic", "Dark"],
                            "Ghost": ["Ghost", "Psychic"],
                            "Steel": ["Rock", "Ice", "Fairy"],
                            "Fire": ["Bug", "Steel", "Grass", "Ice"],
                            "Water": ["Ground", "Rock", "Fire"],
                            "Grass": ["Ground", "Rock", "Water"],
                            "Electric": ["Flying", "Water"],
                            "Psychic": ["Fighting", "Poison"],
                            "Ice": ["Flying", "Ground", "Grass", "Dragon"],
                            "Dragon": ["Dragon"],
                            "Dark": ["Ghost", "Psychic"],
                            "Fairy": ["Fighting", "Dragon", "Dark"]
                            }


table_des_types_peu_efficace = {
                            "Normal": ["Rock", "Steel"],
                            "Fighting": ["Flying", "Poison", "Bug", "Ghost", "Psychic", "Fairy"],
                            "Flying": ["Rock", "Steel", "Electric"],
                            "Poison": ["Poison", "Ground", "Rock", "Ghost", "Steel"],
                            "Ground": ["Flying", "Bug", "Grass"],
                            "Rock": ["Fighting", "Ground", "Steel"],
                            "Bug": ["Fighting", "Flying", "Poison", "Ghost", "Steel", "Fire", "Fairy"],
                            "Ghost": ["Normal", "Dark"],
                            "Steel": ["Steel", "Fire", "Water", "Electric"],
                            "Fire": ["Rock", "Fire", "Water", "Dragon"],
                            "Water": ["Water", "Grass", "Dragon"],
                            "Grass": ["Flying", "Poison", "Bug", "Steel", "Fire", "Grass", "Dragon"],
                            "Electric": ["Ground", "Grass", "Electric", "Dragon"],
                            "Psychic": ["Steel", "Psychic"],
                            "Ice": ["Steel", "Fire", "Water", "Ice"],
                            "Dragon": ["Fairy", "Steel"],
                            "Dark": ["Fighting", "Dark", "Fairy"],
                            "Fairy": ["Poison", "Steel", "Fire"]
                            }


def soin(pokemons, fenetre1, fenetre2, joueur):

    for i in pokemons:
        sql_methode.modif_stat_poke(i, "current_hp", 9999)

    fenetre1.destroy()
    fenetre2.destroy()


    joelle = Tk()
    joelle.title("Infirmière Joëlle")
    joelle.resizable(width = False, height = False)

    Label(joelle, text = "Merci de votre attente et de votre fidélité au près de notre centre!\n"+
                            "Vos pokémons sont maintenant soignés, j'espère vous revoir, enfin pas trop vite quand même!", font = ('Arial', 10)).pack(pady=10)


    centre_pokemon = Tk()
    centre_pokemon.title("Centre Pokémon")
    centre_pokemon.geometry("400x800")
    centre_pokemon.resizable(width=False, height=False)

    pc_id = joueur.get_equipe()
    n_pc_id = sql_methode.get_id_pokemon(pc_id)
    sprites = sql_methode.sprites(centre_pokemon)

    image = PhotoImage(master = joelle, file = "bg\joelle.png")
    Label(joelle, image = image).pack()

    stats = []
    for z in pc_id:
        stats.append(sql_methode.get_stat_poke_joueur(z))

    var = 0
    y = 105
    for i in n_pc_id:

        Label(centre_pokemon, image = sprites[i[0]]).pack(pady = 10)
        Label(centre_pokemon, text = str(stats[var]["nom"]) + "    Niv " + str(stats[var]["niveau"])).pack()
        Label(centre_pokemon, text = str(stats[var]["current_hp"]) + " / " + str(stats[var]["hp"])).pack()
        var+=1

    joelle.after(3000, lambda: partir(joelle,centre_pokemon))

    joelle.mainloop()
    centre_pokemon.mainloop()
def partir(fenetre1, fenetre2):
    fenetre1.destroy()
    fenetre2.destroy()


def buy(id_objet, id_joueur, argent):

    info = sql_methode.info_joueur(id_joueur)

    if id_objet == 1 and info[6] >= 100:
        sql_methode.get_objet(id_joueur, "Pokeball", "pokeball")
        sql_methode.update_golds(id_joueur, -100)
        info = sql_methode.info_joueur(id_joueur)
        argent.configure(text = "Or: "+str(info[6]))
    elif id_objet == 2 and info[6] >= 600:
        sql_methode.get_objet(id_joueur, "SuperBall", "pokeball")
        sql_methode.update_golds(id_joueur, -600)
        info = sql_methode.info_joueur(id_joueur)
        argent.configure(text = "Or: "+str(info[6]))
    elif id_objet == 3 and info[6] >= 800:
        sql_methode.get_objet(id_joueur, "HyperBall", "pokeball")
        sql_methode.update_golds(id_joueur, -800)
        info = sql_methode.info_joueur(id_joueur)
        argent.configure(text = "Or: "+str(info[6]))

    elif id_objet == 4 and info[6] >= 300:
        sql_methode.get_objet(id_joueur, "Potion", "Potion")
        sql_methode.update_golds(id_joueur, -300)
        info = sql_methode.info_joueur(id_joueur)
        argent.configure(text = "Or: "+str(info[6]))
    elif id_objet == 5 and info[6] >= 700:
        sql_methode.get_objet(id_joueur, "Super Potion", "Potion")
        sql_methode.update_golds(id_joueur, -700)
        info = sql_methode.info_joueur(id_joueur)
        argent.configure(text = "Or: "+str(info[6]))
    elif id_objet == 6 and info[6] >= 1500:
        sql_methode.get_objet(id_joueur, "Hyper Potion", "Potion")
        sql_methode.update_golds(id_joueur, -1500)
        info = sql_methode.info_joueur(id_joueur)
        argent.configure(text = "Or: "+str(info[6]))
    elif id_objet == 7 and info[6] >= 2500:
        sql_methode.get_objet(id_joueur, "Potion Max", "Potion")
        sql_methode.update_golds(id_joueur, -2500)
        info = sql_methode.info_joueur(id_joueur)
        argent.configure(text = "Or: "+str(info[6]))

    else:
        vendeur = Tk()
        vendeur.title("Vendeur Yoan")
        vendeur.resizable(width = False, height = False)

        Label(vendeur, text = "Désolé! mais votre nombre d'Or est insuffisant pour acheter cet article!", font = ('Arial', 10)).pack(pady=10)

        image = PhotoImage(master = vendeur, file = "bg\pendeur.png")
        Label(vendeur, image = image).pack()

        vendeur.after(1800, lambda: vendeur.destroy())
        vendeur.mainloop()
def aurevoir(fenetre1):

        vendeur = Tk()
        vendeur.title("Vendeur Yoan")
        vendeur.resizable(width = False, height = False)

        Label(vendeur, text = "J'èspere que cette visite vous aura plu! J'ai hâte de la prôchaine!", font = ('Arial', 10)).pack(pady=10)

        image = PhotoImage(master = vendeur, file = "bg\pendeur.png")
        Label(vendeur, image = image).pack()

        vendeur.after(3000, lambda: partir(fenetre1, vendeur))
        vendeur.mainloop()


def bascule_rencontre(b_rencontre, id):

        rencontre = sql_methode.poke_rencontre()

        r = []
        for i in rencontre:
            r.append(i[0])
        rencontre = r

        if id not in rencontre:
            b_rencontre.configure(text = "Accepter que les autres pokémon\npuissent rencontrer le votre",
                                    command = lambda: [sql_methode.modif_stat_poke(id, "rencontre", True), bascule_rencontre(b_rencontre, id)])
        else:
            b_rencontre.configure(text = "Refuser que les autres pokémon\npuissent rencontrer le votre",
                                   command = lambda: [sql_methode.modif_stat_poke(id, "rencontre", False), bascule_rencontre(b_rencontre, id)])
def resume_rencontre(id, idpokemon_joueur):

    info = Tk()
    info.title("Résumé")
    info.resizable(width=False, height=False)

    info["padx"] = 120
    info["pady"] = 10

    stats = sql_methode.get_stat_poke_joueur(id)
    joueur_info = sql_methode.get_id_joueur(id)

    Label(info, text = "Pokémon de: {}".format(joueur_info[1]), font = ('Arial Black', 10)).pack(pady = 10)

    Label(info, text = "Nom", font = ('Arial Black', 10)).pack()
    Label(info, text = stats["nom"], font = ('Arial', 10)).pack(pady = 10)

    Label(info, text = "Level", font = ('Arial Black', 10), fg = "Orange").pack()
    Label(info, text = stats["niveau"], font = ('Arial', 10)).pack(pady = 10)

    Label(info, text = "Hp", font = ('Arial Black', 10), fg = "Green").pack()
    Label(info, text = stats["hp"], font = ('Arial', 10)).pack(pady = 10)

    Label(info, text = "Attaque", font = ('Arial Black', 10), fg = "Red").pack()
    Label(info, text = stats["atk"], font = ('Arial', 10)).pack(pady = 10)

    Label(info, text = "Defense", font = ('Arial Black', 10), fg = "Blue").pack()
    Label(info, text = stats["def"], font = ('Arial', 10)).pack(pady = 10)

    Label(info, text = "Attaque Spéciale", font = ('Arial Black', 10), fg = "Red").pack()
    Label(info, text = stats["sp_atk"], font = ('Arial', 10)).pack(pady = 10)

    Label(info, text = "Défense Spéciale", font = ('Arial Black', 10), fg = "Blue").pack()
    Label(info, text = stats["sp_def"], font = ('Arial', 10)).pack(pady = 10)

    Label(info, text = "Vitesse", font = ('Arial Black', 10), fg = "Pink").pack()
    Label(info, text = stats["spd"], font = ('Arial', 10)).pack(pady = 10)

    Label(info, text = "Talent", font = ('Arial Black', 10), fg = "Orange").pack()
    Label(info, text = stats["talent"], font = ('Arial', 10)).pack(pady = 10)

    Button(info, text = "Affinité", command = lambda: action_fen(info, id, idpokemon_joueur)).pack(pady=10)

    info.mainloop()
def action_fen(fenetre, idpokemon1, idpokemon2):

    fenetre.destroy()

    actiontk = Tk()
    actiontk.title("Résumé")
    actiontk.resizable(width=False, height=False)

    actiontk["padx"] = 120
    actiontk["pady"] = 10

    affinite, color = aff_recup(idpokemon1, idpokemon2)
    if affinite == []:
        sql_methode.new_affinite(idpokemon1, idpokemon2)
        affinite, color = aff_recup(idpokemon1, idpokemon2)
    info1 = sql_methode.get_stat_poke_joueur(idpokemon1)
    info2 = sql_methode.get_stat_poke_joueur(idpokemon2)


    Label(actiontk, text = "Affinité entre {} et {}".format(info1["nom"], info2["nom"]), font = ('Arial Black', 10)).pack()
    l1 = Label(actiontk, text = str(affinite[0])+"%", font = ('Arial', 10), fg = color)
    l1.pack(pady = 10)

    Label(actiontk, text = "Nombre d'actions possible", font = ('Arial Black', 10)).pack()
    l2 = Label(actiontk, text = str(affinite[1]), font = ('Arial', 10))
    l2.pack(pady = 10)

    b1=Button(actiontk, text = "Se parler [1]", command = lambda: action(idpokemon1, idpokemon2, 0, affinite[1], b, l))
    b1.pack(pady = 10)
    b2=Button(actiontk, text = "Comparer leur force [3]", command = lambda: action(idpokemon1, idpokemon2, 1, affinite[1], b, l))
    b2.pack(pady = 10)
    b3=Button(actiontk, text = "Caresser l'autre [1]", command = lambda: action(idpokemon1, idpokemon2, 2, affinite[1], b, l))
    b3.pack(pady = 10)
    b4=Button(actiontk, text = "Chasser ensemble [5]", command = lambda: action(idpokemon1, idpokemon2, 3, affinite[1], b, l))
    b4.pack(pady = 10)
    b5=Button(actiontk, text = "Jouer à saute mouton [3]", command = lambda: action(idpokemon1, idpokemon2, 4, affinite[1], b, l))
    b5.pack(pady = 10)

    l = [l1, l2]
    b = [b1, b2, b3, b4, b5]

    if affinite[1] < 1:
        b[0].configure(state = DISABLED)
        b[2].configure(state = DISABLED)
    if affinite[1] < 3:
        b[1].configure(state = DISABLED)
        b[4].configure(state = DISABLED)
    if affinite[1] < 5:
        b[3].configure(state = DISABLED)
def action(idpokemon1, idpokemon2, id, nbr_actions, b, l):

    if id == 0 and nbr_actions >= 1:

        a = randint(1, 100)
        if a < 90:
            sql_methode.modif_affinite(idpokemon1, idpokemon2, 2, -1)
            affinite, color = aff_recup(idpokemon1, idpokemon2)
        else:
            sql_methode.modif_affinite(idpokemon1, idpokemon2, -2, -1)
            affinite, color = aff_recup(idpokemon1, idpokemon2)

        l[0].configure(text = str(affinite[0])+"%", fg = color)
        l[1].configure(text = str(affinite[1]))

    if id == 1:

        a = randint(1, 100)
        if a < 65:
            sql_methode.modif_affinite(idpokemon1, idpokemon2, 6, -3)
            affinite, color = aff_recup(idpokemon1, idpokemon2)
        else:
            sql_methode.modif_affinite(idpokemon1, idpokemon2, -6, -3)
            affinite, color = aff_recup(idpokemon1, idpokemon2)

        l[0].configure(text = str(affinite[0])+"%", fg = color)
        l[1].configure(text = str(affinite[1]))

    if id == 2:

        a = randint(1, 100)
        if a < 85:
            sql_methode.modif_affinite(idpokemon1, idpokemon2, 3, -1)
            affinite, color = aff_recup(idpokemon1, idpokemon2)
        else:
            sql_methode.modif_affinite(idpokemon1, idpokemon2, -3, -1)
            affinite, color = aff_recup(idpokemon1, idpokemon2)

        l[0].configure(text = str(affinite[0])+"%", fg = color)
        l[1].configure(text = str(affinite[1]))

    if id == 3:

        a = randint(1, 100)
        if a < 45 :
            sql_methode.modif_affinite(idpokemon1, idpokemon2, 10, -5)
            affinite, color = aff_recup(idpokemon1, idpokemon2)
        else:
            sql_methode.modif_affinite(idpokemon1, idpokemon2, -10, -5)
            affinite, color = aff_recup(idpokemon1, idpokemon2)

        l[0].configure(text = str(affinite[0])+"%", fg = color)
        l[1].configure(text = str(affinite[1]))

    if id == 4:

        a = randint(1, 100)
        if a < 55:
            sql_methode.modif_affinite(idpokemon1, idpokemon2, 5, -3)
            affinite, color = aff_recup(idpokemon1, idpokemon2)
        else:
            sql_methode.modif_affinite(idpokemon1, idpokemon2, -5, -3)
            affinite, color = aff_recup(idpokemon1, idpokemon2)

        l[0].configure(text = str(affinite[0])+"%", fg = color)
        l[1].configure(text = str(affinite[1]))


    if affinite[1] < 1:
        b[0].configure(state = DISABLED)
        b[2].configure(state = DISABLED)
    if affinite[1] < 3:
        b[1].configure(state = DISABLED)
        b[4].configure(state = DISABLED)
    if affinite[1] < 5:
        b[3].configure(state = DISABLED)
def aff_recup(idpokemon1, idpokemon2):

    affinite = sql_methode.get_affinite(idpokemon1, idpokemon2)
    color = ""

    if len(affinite) != 0:
        r = []
        for i in affinite[0]:
            r.append(i)
        affinite = r

        if affinite[0] == 0:
            color = "Blue"
        elif 0 > affinite[0] < 20:
            color = "Red"
        elif 20 >= affinite[0] < 50:
            color = "Orange"
        elif 50 >= affinite[0] < 80:
            color = "Yellow"
        elif affinite[0] == 100:
            color = "#FF78CB"
        elif 0 > affinite[0] <= -50:
            color = "#8B0000"
        elif -50 > affinite[0] <= -100:
            color = "Black"

    return affinite, color
def jenny_txt(fenetre):

    jenny = Tk()
    jenny.title("Agent Jenny")
    jenny.resizable(width = False, height = False)

    image1 = PhotoImage(master = jenny, file = "bg\Agent_Jenny.png")

    Label(jenny, text = "Oh! vous partez? j'espère que votre pokémon c'est bien amusé!", font = ('Arial', 10)).pack(pady=10)
    Label(jenny, image = image1).pack()
    jenny.after(3000, lambda : partir(jenny, fenetre))

    jenny.mainloop()


def ev_buy(id, joueur, stat, nbr_ev, prix, money, argent, stats_poke, ev):

        stats = sql_methode.get_stat_poke_joueur(id)
        stats_j = sql_methode.info_joueur(joueur.get_id())

        ev_dispo = stats["ev"]
        money = stats_j[6]

        if money >= prix and ev_dispo >= nbr_ev:
            sql_methode.modif_stat_poke(id, stat, nbr_ev)
            sql_methode.update_golds(joueur.get_id(), -prix)

            stats = sql_methode.get_stat_poke_joueur(id)
            stats_j = sql_methode.info_joueur(joueur.get_id())

            argent.configure(text = "Or: "+str(stats_j[6]))
            stats_poke.configure(text = "{} -> {}, {}, {}, {}, {}, {}".format(
                                stats["nom"], stats["hp"], stats["atk"], stats["def"], stats["sp_atk"], stats["sp_def"], stats["spd"]))
            ev.configure(text = "Ev dispo: "+str(stats["ev"]))
        elif ev_dispo < nbr_ev:
            matthias = Tk()
            matthias.title("Entraîneur Matthias")
            matthias.resizable(width = False, height = False)

            Label(matthias, text = "Ton pokémon est déjà assez fort !\nTu ne peux plus l'entraîner avec ce sac.", font = ('Arial', 10)).pack(pady=10)

            imageM = PhotoImage(master = matthias, file = "bg\entraineur_matthias.png")
            Label(matthias, image = imageM).pack()
            matthias.after(3000, lambda : matthias.destroy())

            matthias.mainloop()
def matthias_txt(fenetre):

        matthias = Tk()
        matthias.title("Entraîneur Matthias")
        matthias.resizable(width = False, height = False)

        Label(matthias, text = "Tu pars mec !? N'oublie pas que si je te vois à l'arène je te ferais pas de cadeau !", font = ('Arial', 10)).pack(pady=10)

        imageM = PhotoImage(master = matthias, file = "bg\entraineur_matthias.png")
        Label(matthias, image = imageM).pack()
        matthias.after(3000, lambda : partir(matthias, fenetre))

        matthias.mainloop()

def cantineA(id, idpokemon, idjoueur, argent, nbr, prix = 5000):

    can = sql_methode.cantine_get(idpokemon)

    if len(can) == 2:
        angel_txt(0)
    elif len(can) == 1 and id == can[0][1]:
        angel_txt(0)
    elif id == 6:
        ran = randint(0, 5)
        if len(can) == 1:
            while ran == can[0][1]:
                ran = randint(0, 5)

        if ran == 0:
            nbr = 150

        sql_methode.cantine_insert(idpokemon, ran, nbr)
        sql_methode.modif_stat_poke(idpokemon, ran, nbr)
        sql_methode.update_golds(idjoueur, -prix)

        p = sql_methode.info_joueur(idjoueur)
        argent.configure(text = "Or: "+str(p[6]))


    else:
        sql_methode.cantine_insert(idpokemon, id, nbr)
        sql_methode.modif_stat_poke(idpokemon, id, nbr)
        sql_methode.update_golds(idjoueur, -prix)

        p = sql_methode.info_joueur(idjoueur)
        argent.configure(text = "Or: "+str(p[6]))
def angel_txt(id, fenetre = 0):

        if id == 0:
            angel = Tk()
            angel.title("Dresseur Angel")
            angel.resizable(width = False, height = False)

            Label(angel, text = "HÉÉÉÉÉÉÉÉÉ!!!!\nJe te vois, ne mange pas plus ce que qui est autorisé!", font = ('Arial', 10)).pack(pady=10)

            imageM = PhotoImage(master = angel, file = "bg\dresseur_angel.png")
            Label(angel, image = imageM).pack()
            angel.after(3000, lambda : angel.destroy())

            angel.mainloop()

        else:

            angel = Tk()
            angel.title("Dresseur Angel")
            angel.resizable(width = False, height = False)

            Label(angel, text = "Ah bah enfin tu pars!\nMoi aussi j'ai faim!", font = ('Arial', 10)).pack(pady=10)

            imageM = PhotoImage(master = angel, file = "bg\dresseur_angel.png")
            Label(angel, image = imageM).pack()
            angel.after(3000, lambda : partir(angel, fenetre))

            angel.mainloop()


def battle(terrain, joueur, b, idpokemon1, idpokemon2, level, tour =0, vs_joueur = False, in_battle = False, stat1 = 0, stat2 = 0, inflige = 0):

    fight = Tk()
    fight.title("Battle")
    fight.geometry("680x460")
    fight.resizable(width = False, height = False)

    sprites = sql_methode.sprites(fight)
    id_sprite1 = sql_methode.get_id_pokemon([idpokemon1])

    if not in_battle:
        stat1 = sql_methode.get_stat_poke_joueur(idpokemon1)

        stat2 = sql_methode.get_stats_poke_non_joueur(idpokemon2, level)
        stat2["current_hp"] = stat2["hp"]

        if stat1["spd"] > stat2["spd"]:
            tour = 1
        else:
            tour = 2

    t2 = False
    if stat1["types"][1] != None:
        t2 = True

    print(tour, vs_joueur)
    image1 = sprites[id_sprite1[0][0]]
    image2 = sprites[idpokemon2]
    Label(fight, image = image1).place(x=120, y=100)
    Label(fight, image = image2).place(x=512, y=100)

    Label(fight, text = str(stat1["current_hp"])+"/"+str(stat1["hp"])).place(x=135, y=172)
    Label(fight, text = str(stat2["current_hp"])+"/"+str(stat2["hp"])).place(x=527, y=170)
    Label(fight, text = str(stat2["nom"])+ " -> " +str(stat2["niveau"])).place(x=515, y=200)
    Label(fight, text = "Ce pokémon vous a ingligé: "+str(inflige)+" dégats").place(x=440, y=250)

    button_next = Button(fight, text = "Next Move", state = DISABLED)
    button_next.place(x=316, y=60)
    button_quit = Button(fight, text = "Fuir !", command = lambda: fuite(b, fight, idpokemon1, stat1))
    button_quit.place(x=525, y=300)

    if not vs_joueur:
        button_cap = Button(fight, text = "Capture", command = lambda: capture(idpokemon1, idpokemon2, stat2["niveau"], stat1, stat2, inflige, fight, b, joueur, terrain, vs_joueur = vs_joueur))
        button_cap.place(x=515, y=350)
    atk_type1 = Button(fight, text = str(stat1["types"][0])+" ["+str(stat1["atk"])+" Atk]", command = lambda: degats(terrain, joueur, b,tour, fight, idpokemon1, idpokemon2, stat1, stat2, "atk", "def", 0, inflige, vs_joueur = vs_joueur))
    atk_type1.place(x=20, y=220)
    sp_atk_type1 = Button(fight, text = str(stat1["types"][0])+" ["+str(stat1["sp_atk"])+" Sp_Atk]", command = lambda: degats(terrain, joueur, b,tour, fight, idpokemon1, idpokemon2, stat1, stat2, "sp_atk", "sp_def", 0, inflige, vs_joueur = vs_joueur))
    sp_atk_type1.place(x=10, y=260)
    if t2:
        atk_type2 = Button(fight, text = str(stat1["types"][1])+" ["+str(stat1["atk"])+" Atk]", command = lambda: degats(terrain, joueur, b,tour, fight, idpokemon1, idpokemon2, stat1, stat2, "atk", "def", 1, inflige, vs_joueur = vs_joueur))
        atk_type2.place(x=190, y=220)
        sp_atk_type2 = Button(fight, text = str(stat1["types"][1])+" ["+str(stat1["sp_atk"])+" Sp_Atk]", command = lambda: degats(terrain, joueur, b,tour, fight, idpokemon1, idpokemon2, stat1, stat2, "sp_atk", "sp_def", 1, inflige, vs_joueur = vs_joueur))
        sp_atk_type2.place(x=180, y=260)


    if tour == 2:
        atk_type1.configure(state = DISABLED)
        sp_atk_type1.configure(state = DISABLED)
        if t2:
            atk_type2.configure(state = DISABLED)
            sp_atk_type2.configure(state = DISABLED)
        if not vs_joueur:
            button_cap.configure(state = DISABLED)
        button_next.configure(state = NORMAL, command = lambda:degats(terrain, joueur, b,tour, fight, idpokemon1, idpokemon2, stat1, stat2, "", "", "", inflige, vs_joueur = vs_joueur))

    else:
        atk_type1.configure(state = NORMAL)
        sp_atk_type1.configure(state = NORMAL)
        if t2:
            atk_type2.configure(state = NORMAL)
            sp_atk_type2.configure(state = NORMAL)


    fight.mainloop()
def degats(terrain, joueur, but, tour, fight, idpokemon1, idpokemon2, stat1, stat2, sp, sp_def, types, w, vs_joueur):

    a,b,c,d = 1,1,1,1
    if tour == 1:
        tour = 2

        a = stat1[sp]-stat2[sp_def]
        if a < 0:
            a = 1

        if stat2["types"][0] in table_des_types_efficace[stat1["types"][types]]:
            a = a * 2
        if stat2["types"][1] != None:
            if stat2["types"][1] in table_des_types_efficace[stat1["types"][types]]:
                a = a * 2
        if stat2["types"][0] in table_des_types_peu_efficace[stat1["types"][types]]:
            a = a * 0.5
        if stat2["types"][1] != None:
            if stat2["types"][1] in table_des_types_peu_efficace[stat1["types"][types]]:
                a = a * 0.5

        stat2["current_hp"] -= a

    else:

        tour = 1
        a = stat2["atk"]-stat1["def"]
        if a < 0:
            a = 1

        if stat1["types"][0] in table_des_types_efficace[stat2["types"][0]]:
            a = a * 2
        if stat1["types"][1] != None:
            if stat1["types"][1] in table_des_types_efficace[stat2["types"][0]]:
                a = a * 2
        if stat1["types"][0] in table_des_types_peu_efficace[stat2["types"][0]]:
            a = a * 0.5
        if stat1["types"][1] != None:
            if stat1["types"][1] in table_des_types_peu_efficace[stat2["types"][0]]:
                a = a * 0.5

        if stat2["types"][1] != None:
            b = stat2["atk"]-stat1["def"]
            if b < 0:
                b = 1

            if stat1["types"][0] in table_des_types_efficace[stat2["types"][1]]:
                b = b * 2
            if stat1["types"][1] != None:
                if stat1["types"][1] in table_des_types_efficace[stat2["types"][1]]:
                    b = b * 2
            if stat1["types"][0] in table_des_types_peu_efficace[stat2["types"][1]]:
                b = b * 0.5
            if stat1["types"][1] != None:
                if stat2["types"][1] in table_des_types_peu_efficace[stat2["types"][1]]:
                    b = b * 0.5

        c = stat2["sp_atk"]-stat1["sp_def"]
        if c < 0:
            c = 1

        if stat1["types"][0] in table_des_types_efficace[stat2["types"][0]]:
            c = c * 2
        if stat1["types"][1] != None:
            if stat2["types"][1] in table_des_types_efficace[stat2["types"][0]]:
                c = c * 2
        if stat1["types"][0] in table_des_types_peu_efficace[stat2["types"][0]]:
            c = c * 0.5
        if stat1["types"][1] != None:
            if stat2["types"][1] in table_des_types_peu_efficace[stat2["types"][0]]:
                c = c * 0.5

        if stat2["types"][1] != None:
            d = stat2["sp_atk"]-stat1["sp_def"]
            if d < 0:
                d = 1

            if stat1["types"][0] in table_des_types_efficace[stat2["types"][1]]:
                d = d * 2
            if stat1["types"][1] != None:
                if stat1["types"][1] in table_des_types_efficace[stat2["types"][1]]:
                    d = d * 2
            if stat1["types"][0] in table_des_types_peu_efficace[stat2["types"][1]]:
                d = d * 0.5
            if stat1["types"][1] != None:
                if stat2["types"][1] in table_des_types_peu_efficace[stat2["types"][1]]:
                    d = d * 0.5

        w = max(a, b, c, d)
        stat1["current_hp"] -= w

    fight.destroy()


    if tour == 2 and stat2["current_hp"] > 0:
        battle(terrain, joueur, but, idpokemon1, idpokemon2, 0, tour, in_battle = True, stat1 = stat1, stat2 = stat2, inflige=w, vs_joueur = vs_joueur)
    elif tour == 1 and stat1["current_hp"] > 0:
        battle(terrain, joueur, but, idpokemon1, idpokemon2, 0, tour, in_battle = True, stat1 = stat1, stat2 = stat2, inflige=w, vs_joueur = vs_joueur)
    elif stat2["current_hp"] <= 0:
        fin_battle(terrain, but, True, idpokemon1, stat1)
    else:
        fin_battle(terrain, but, False, idpokemon1, stat1)
def fin_battle(terrain, but, win, idpokemon1, stat1):

    prof = Tk()
    prof.title("Professeur Maimone")
    prof.resizable(width=False, height=False)

    if win:
        Label(prof, text="GG! Tu as vaincu le pokémon ennemi.", font = ('Arial', 10)).pack(pady=10, padx = 5)
        sql_methode.set_level_up(idpokemon1)
        sql_methode.update_golds(stat1["idjoueur"], 500)
        prof.after(4000, lambda:(prof.destroy(), sql_methode.modif_stat_poke(idpokemon1, "current_hp", -(stat1["hp"]-stat1["current_hp"])), but.configure(state=DISABLED)))
    else:
        Label(prof, text="Bah !? On perd a ce que je vois.", font = ('Arial', 10)).pack(pady=10, padx = 5)
        sql_methode.update_golds(stat1["idjoueur"], -300)
        prof.after(4000, lambda:(prof.destroy(), sql_methode.modif_stat_poke(idpokemon1, "current_hp", -(stat1["hp"]-stat1["current_hp"]))))
        terrain.destroy()

    image = PhotoImage(master = prof, file = "bg\professeur_maimonec.png")
    Label(prof, image = image).pack()


    prof.mainloop()
def fuite(b, fenetre, idpokemon1, stat1):

    prof = Tk()
    prof.title("Professeur Maimone")
    prof.resizable(width=False, height=False)


    Label(prof, text="Tu t'enfuis !?\nDes fois c'est vrai que c'est préférable, mais porte tes couilles !", font = ('Arial', 10)).pack(pady=10, padx = 5)
    image = PhotoImage(master = prof, file = "bg\professeur_maimonec.png")
    Label(prof, image = image).pack()


    prof.after(4000, lambda:(partir(prof, fenetre), sql_methode.modif_stat_poke(idpokemon1, "current_hp", -(stat1["hp"]-stat1["current_hp"])), b.configure(state=DISABLED)))
    prof.mainloop()
def capture(idpokemon1, idpokemon2, level, stat1, stat2, inflige, fenetre, b, joueur, terrain):

    a = randint(1,100)
    fenetre.destroy()

    if a >= 60:
        joueur.capture(level, idpokemon2)

        prof = Tk()
        prof.title("Professeur Maimone")
        prof.resizable(width=False, height=False)


        Label(prof, text="Bravo! Tu as capturé le pokémon!", font = ('Arial', 10)).pack(pady=10, padx = 5)
        image = PhotoImage(master = prof, file = "bg\professeur_maimonec.png")
        Label(prof, image = image).pack()

        sql_methode.modif_stat_poke(idpokemon1, "current_hp", -(stat1["hp"]-stat1["current_hp"]))
        prof.after(4000, lambda:(prof.destroy(), b.configure(state=DISABLED)))
        prof.mainloop()

    else:

        prof = Tk()
        prof.title("Professeur Maimone")
        prof.resizable(width=False, height=False)


        Label(prof, text="Dommage tu as raté ta capture!", font = ('Arial', 10)).pack(pady=10, padx = 5)
        image = PhotoImage(master = prof, file = "bg\professeur_maimonec.png")
        Label(prof, image = image).pack()


        prof.after(2000, lambda:(prof.destroy(),battle(terrain, joueur, b, idpokemon1, idpokemon2, level, 2, stat1=stat1, stat2=stat2, inflige=inflige, in_battle = True)))
        prof.mainloop()


