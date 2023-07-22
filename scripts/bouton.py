from cgitb import text
from logging import root
from tkinter import *
from bouton_methodes import *
import sql_methode

def creation_button(fenetre_general, joueur):

    image1 = PhotoImage(master = fenetre_general, file = "bg\centre_p.png")
    bouton=Button(fenetre_general, image = image1, command= lambda: create(0, joueur))
    bouton.place(x = 207, y = 41)

    image2 = PhotoImage(master = fenetre_general, file = "bg\herbes.png")
    bouton=Button(fenetre_general, image = image2, command = lambda: joueur.pokemon_in_salle(1))
    bouton.place(x = 342, y = 0)

    image3 = PhotoImage(master = fenetre_general, file = "bg\defis.png")
    bouton=Button(fenetre_general, image = image3, command = lambda: joueur.pokemon_in_salle(2))
    bouton.place(x = 175, y = 336)

    image4 = PhotoImage(master = fenetre_general, file = "bg\s_rencontre.png")
    bouton=Button(fenetre_general, image = image4, command = lambda: joueur.pokemon_in_salle(3))
    bouton.place(x = 558, y = 324)

    image5 = PhotoImage(master = fenetre_general, file = "bg\cantine.png")
    bouton=Button(fenetre_general, image = image5, command = lambda: joueur.pokemon_in_salle(4))
    bouton.place(x = 174, y = 223)

    image6 = PhotoImage(master = fenetre_general, file = "bg\s_sport.png")
    bouton = Button(fenetre_general, image = image6, command = lambda: joueur.pokemon_in_salle(5))
    bouton.place(x = 432, y = 342)

    image7 = PhotoImage(master = fenetre_general, file = "bg\shop.png")
    bouton = Button(fenetre_general, image = image7, command = lambda: create(6, joueur))
    bouton.place(x = 431, y = 225)

    fenetre_general.mainloop()

def create(id, joueur, idpokemon=0):

    #centre pokemon
    if id == 0:

        joelle = Tk()
        joelle.title("Infirmière Joëlle")
        joelle.resizable(width = False, height = False)

        Label(joelle, text = "Bienvenue dresseur! Voulez-vous soigner vos pokémons?", font = ('Arial', 10)).pack(pady=10)


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

        Button(joelle, text = "Soigner", command = lambda : soin(pc_id, joelle, centre_pokemon, joueur)).pack(pady = 10)
        Button(joelle, text = "Non c'est bon enfaite", command = lambda : partir(joelle, centre_pokemon)).pack(pady = 10)

        joelle.mainloop()
        centre_pokemon.mainloop()

    #terrain
    elif id == 1:

        st = sql_methode.get_stat_poke_joueur(idpokemon)

        if st["current_hp"] > 0:

            prof = Tk()
            prof.title("Professeur Maimone")
            prof.resizable(width=False, height=False)


            Label(prof, text="Oh tu pars !? Les gens du village et moi attendrons ton retour avec impatience !", font = ('Arial', 10)).pack(pady=10)
            image = PhotoImage(master = prof, file = "bg\professeur_maimonec.png")
            Label(prof, image = image).pack()

            terrain = Tk()
            terrain.title("Terrain")
            terrain["pady"] = 20
            terrain["padx"] = 120
            terrain.resizable(width=False, height=False)

            sprites = sql_methode.sprites(terrain)
            niv = sql_methode.get_stat_poke_joueur(idpokemon)

            if niv["niveau"] > 50:
                min = niv["niveau"]-5
                if min < 0:
                    min = 1

                max = niv["niveau"]+20
                if max > 100:
                    max = 100
            else:
                min = niv["niveau"]-4
                if min < 0:
                    min = 1

                max = niv["niveau"]+3
                if max > 100:
                    max = 100

            pokemonsauvage=[]
            for i in range(7):
                ran = randint(1, 894)
                level = randint(min, max)
                pokemonsauvage.append([ran, level])

            for i in pokemonsauvage:

                if i == pokemonsauvage[0]:
                    a = [i[0], i[1]]
                    b1 = Button(terrain, image = sprites[i[0]], command=lambda:battle(terrain, joueur, b1, idpokemon, a[0], a[1]))
                    b1.pack()
                if i == pokemonsauvage[1]:
                    b = [i[0], i[1]]
                    b2 = Button(terrain, image = sprites[i[0]], command=lambda:battle(terrain, joueur, b2, idpokemon, b[0], b[1]))
                    b2.pack()
                if i == pokemonsauvage[2]:
                    c = [i[0], i[1]]
                    b3 = Button(terrain, image = sprites[i[0]], command=lambda:battle(terrain, joueur, b3, idpokemon, c[0], c[1]))
                    b3.pack()
                if i == pokemonsauvage[3]:
                    d = [i[0], i[1]]
                    b4 = Button(terrain, image = sprites[i[0]], command=lambda:battle(terrain, joueur, b4, idpokemon, d[0], d[1]))
                    b4.pack()
                if i == pokemonsauvage[4]:
                    e = [i[0], i[1]]
                    b5 = Button(terrain, image = sprites[i[0]], command=lambda:battle(terrain, joueur, b5, idpokemon, e[0], e[1]))
                    b5.pack()
                if i == pokemonsauvage[5]:
                    f = [i[0], i[1]]
                    b6 = Button(terrain, image = sprites[i[0]], command=lambda:battle(terrain, joueur, b6, idpokemon, f[0], f[1]))
                    b6.pack()
                if i == pokemonsauvage[6]:
                    g = [i[0], i[1]]
                    b7 = Button(terrain, image = sprites[i[0]], command=lambda:battle(terrain, joueur, b7, idpokemon, g[0], g[1]))
                    b7.pack()


            prof.after(4000, lambda:prof.destroy())
            prof.mainloop()
            terrain.mainloop()

        else:

            prof = Tk()
            prof.title("Professeur Maimone")
            prof.resizable(width=False, height=False)


            Label(prof, text="OH! OH! mais ou vas-tu comme cela? Tu ne vois pas que ton pokémon ne peut pas se battre!\nPasse au centre pokémon si tu veux le remettre sur pied.", font = ('Arial', 10)).pack(pady=10)
            image = PhotoImage(master = prof, file = "bg\professeur_maimonec.png")
            Label(prof, image = image).pack()

            prof.after(4000, lambda:prof.destroy())
            prof.mainloop()


    elif id == 2:

        yanhis = Tk()
        yanhis.title("Dresseur de légende Yanhis")
        yanhis.resizable(width=False, height=False)


        Label(yanhis, text="Hmmm !? Ah! c'est toi!\nTu viens te confronter aux maitres de l'arène ? il sont plutôt chaud aujourd'hui.\nHâte qu'on finisse par s'affronter!", font = ('Arial', 10)).pack(pady=10)
        image = PhotoImage(master = yanhis, file = "bg\legende_yanhisc.png")
        Label(yanhis, image = image).pack()


        arene = Tk()
        arene.title("Arène")
        arene.geometry("860x640")
        arene.resizable(width=False, height=False)

        image1 = PhotoImage(master = arene, file = "bg\legende_yanhisp.png")
        image2 = PhotoImage(master = arene, file = "bg\ludwigc.png")
        image3 = PhotoImage(master = arene, file = "bg\parakc.png")

        sprites = sql_methode.sprites(arene)
        niv = sql_methode.get_stat_poke_joueur(idpokemon)

        if niv["niveau"] > 50:
            min = niv["niveau"]-5
            if min < 0:
                min = 1

            max = niv["niveau"]+20
            if max > 100:
                max = 100
        else:
            min = niv["niveau"]-4
            if min < 0:
                min = 1

            max = niv["niveau"]+3
            if max > 100:
                max = 100

        pokemonsauvage=[]
        for i in range(3):
            ran = randint(1, 894)
            level = randint(min, max)
            pokemonsauvage.append([ran, level])

        for i in pokemonsauvage:

            if i == pokemonsauvage[0]:
                a = [i[0], i[1]]
                b1 = Button(arene, image = image1, command=lambda:battle(arene, joueur, b1, idpokemon, a[0], a[1], vs_joueur=True))
                b1.place(x=405, y = 100)
                Label(arene, text="Dresseur de légende Yanhis", font = ('Arial', 10)).place(x=345, y = 210)
            if i == pokemonsauvage[1]:
                b = [i[0], i[1]]
                b2 = Button(arene, image = image2, command=lambda:battle(arene, joueur, b2, idpokemon, b[0], b[1], vs_joueur=True))
                b2.place(x=205, y = 300)
                Label(arene, text="Dresseur de légende Benjamin", font = ('Arial', 10)).place(x=135, y = 410)
            if i == pokemonsauvage[2]:
                c = [i[0], i[1]]
                b3 = Button(arene, image = image3, command=lambda:battle(arene, joueur, b3, idpokemon, c[0], c[1], vs_joueur=True))
                b3.place(x=605, y = 300)
                Label(arene, text="Dresseur de légende Kameto", font = ('Arial', 10)).place(x=565, y = 410)


        yanhis.after(5000, lambda:yanhis.destroy())
        yanhis.mainloop()
        arene.mainloop()

    #Salle de rencontre
    elif id == 3:

        jenny = Tk()
        jenny.title("Agent Jenny")
        jenny.resizable(width = False, height = False)

        Label(jenny, text = "Agent Jenny au rapport! Salle de rencontre, RAS!\nAmusez-vous bien!", font = ('Arial', 10)).pack(pady=10)

        image1 = PhotoImage(master = jenny, file = "bg\Agent_Jenny.png")
        Label(jenny, image = image1).pack()

        salle_de_rencontre = Tk()
        salle_de_rencontre.title("Salle de rencontre")
        salle_de_rencontre.geometry("860x640")
        salle_de_rencontre.resizable(width=False, height=False)

        rencontre = sql_methode.poke_rencontre(False, joueur.get_id())
        sprites = sql_methode.sprites(salle_de_rencontre)

        r = []
        for i in rencontre:
            r.append(i[0])
        rencontre = r

        n_rencontre = sql_methode.get_id_pokemon(rencontre)

        x,y = 860, 640
        x = x//(len(n_rencontre)+2)
        consx=x
        y = y//(len(n_rencontre)+1)
        consy=y+5
        for i in n_rencontre:

            z = rencontre[0]
            eval("Button(salle_de_rencontre, image = sprites[i[0]], command = lambda: resume_rencontre("+str(z)+","+str(idpokemon)+")).place(x=consx, y=consy)")
            consx= consx+x
            rencontre = rencontre[1:len(rencontre)]

            if consx == x * 10:
                consy = consy+y+10
                consx = x


        b_rencontre = Button(salle_de_rencontre, text = "Accepter que les autres pokémon\npuissent rencontrer le votre",)
        b_rencontre.pack(pady = 20)
        Button(salle_de_rencontre, text = "Partir !", command = lambda: jenny_txt(salle_de_rencontre)).place(x=550, y = 30)
        bascule_rencontre(b_rencontre, idpokemon)

        jenny.after(4000, lambda : jenny.destroy())
        jenny.mainloop()
        salle_de_rencontre.mainloop()

    #Cantine
    elif id == 4:

        angel = Tk()
        angel.title("Dresseur Angel")
        angel.resizable(width = False, height = False)

        Label(angel, text = "Tu viens te nourrir avant l'arène?\nAhah, même comme cela tu ne me vaincras pas!", font = ('Arial', 10)).pack(pady=10)

        imageM = PhotoImage(master = angel, file = "bg\dresseur_angel.png")
        Label(angel, image = imageM).pack()


        cantine = Tk()
        cantine.title("Cantine")
        cantine.geometry("680x240")
        cantine.resizable(width=False, height=False)

        stats_j = sql_methode.info_joueur(joueur.get_id())

        argent = Label(cantine, text = "Or: "+str(stats_j[6]), font = ('Arial', 10))
        argent.place(x=15, y=5)

        image = PhotoImage(master = cantine, file = "bg\mepo.png")
        image1 = PhotoImage(master = cantine, file = "bg\pamato.png")
        image2 = PhotoImage(master = cantine, file = "bg\kika.png")
        Button(cantine, image = image, command = lambda: cantineA(0, idpokemon, joueur.get_id(), argent, 100)).place(x=57,y=70)
        Button(cantine, image = image1, command = lambda: cantineA(1, idpokemon, joueur.get_id(), argent, 30)).place(x=174,y=70)
        Button(cantine, image = image2, command = lambda: cantineA(2, idpokemon, joueur.get_id(), argent, 30)).place(x=281,y=70)
        Label(cantine, text="Hp [100]").place(x=52,y=30)
        Label(cantine, text="Atk [30]").place(x=169,y=30)
        Label(cantine, text="Def [30]").place(x=277,y=30)

        image3 = PhotoImage(master = cantine, file = "bg\piguy.png")
        image4 = PhotoImage(master = cantine, file = "bg\pepoi.png")
        image5 = PhotoImage(master = cantine, file = "bg\plga.png")
        Button(cantine, image = image3, command = lambda: cantineA(3, idpokemon, joueur.get_id(), argent, 30)).place(x=348,y=70)
        Button(cantine, image = image4, command = lambda: cantineA(4, idpokemon, joueur.get_id(), argent, 30)).place(x=465,y=70)
        Button(cantine, image = image5, command = lambda: cantineA(5, idpokemon, joueur.get_id(), argent, 30)).place(x=572,y=70)
        Label(cantine, text="Sp_Atk [30]").place(x=338,y=30)
        Label(cantine, text="Sp_Def [30]").place(x=455,y=30)
        Label(cantine, text="Spd [30]").place(x=568,y=30)

        Label(cantine, text="5000Or").place(x=325,y=120)

        image6 = PhotoImage(master = cantine, file = "bg\enigma.png")
        Button(cantine, image = image6, command = lambda: cantineA(6, idpokemon, joueur.get_id(), argent, 50, 10000)).place(x=325,y=160)
        Label(cantine, text="Enigma [150Hp ou 50Stat] -> 10000Or").place(x=260,y=200)

        Button(cantine, text = "Partir", command = lambda: angel_txt(1, cantine)).place(x= 635, y=5)


        angel.after(4000, lambda : angel.destroy())

        angel.mainloop()
        cantine.mainloop()


    #Salle de sport
    elif id == 5:

        matthias = Tk()
        matthias.title("Entraîneur Matthias")
        matthias.resizable(width = False, height = False)

        Label(matthias, text = "Un homme et un pokémon !?\nQu'est-ce j'aimerai vous affronter !\nJe divague encore, fais comme chez toi mec!", font = ('Arial', 10)).pack(pady=10)

        imageM = PhotoImage(master = matthias, file = "bg\entraineur_matthias.png")
        Label(matthias, image = imageM).pack()

        salle_de_sport = Tk()
        salle_de_sport.title("Salle de sport")
        salle_de_sport.geometry("860x640")
        salle_de_sport.resizable(width=False, height=False)

        stats = sql_methode.get_stat_poke_joueur(idpokemon)
        stats_j = sql_methode.info_joueur(joueur.get_id())

        argent = Label(salle_de_sport, text = "Or: "+str(stats_j[6]), font = ('Arial', 10))
        argent.place(x=120, y=30)

        stats_poke = Label(salle_de_sport, text = "{} -> {}, {}, {}, {}, {}, {}".format(
                                stats["nom"], stats["hp"], stats["atk"], stats["def"], stats["sp_atk"], stats["sp_def"], stats["spd"]), font = ('Arial', 10))
        stats_poke.place(x=350, y=30)

        ev = Label(salle_de_sport, text = "Ev dispo: "+str(stats["ev"]), font = ('Arial', 10))
        ev.place(x=700, y =30)

        Button(salle_de_sport, text = "Partir !", command = lambda: matthias_txt(salle_de_sport)).place(x=417, y=60)

        image = PhotoImage(master = salle_de_sport, file = "bg\HP_S.png")
        image1 = PhotoImage(master = salle_de_sport, file = "bg\HP_M.png")
        image2 = PhotoImage(master = salle_de_sport, file = "bg\HP_L.png")
        Button(salle_de_sport, image = image, command = lambda: ev_buy(idpokemon, joueur, 0, 1, 400, stats_j[6], argent, stats_poke, ev)).place(x=143,y=91)
        Button(salle_de_sport, image = image1, command = lambda: ev_buy(idpokemon, joueur, 0, 3, 1000, stats_j[6], argent, stats_poke, ev)).place(x=429,y=91)
        Button(salle_de_sport, image = image2, command = lambda: ev_buy(idpokemon, joueur, 0, 10, 1700, stats_j[6], argent, stats_poke, ev)).place(x=715,y=91)
        Label(salle_de_sport, text="Hp [1] -> 400Or").place(x=110,y=151)
        Label(salle_de_sport, text="Hp [3] -> 1000Or").place(x=396,y=151)
        Label(salle_de_sport, text="Hp [10] -> 1700Or").place(x=682,y=151)

        image3 = PhotoImage(master = salle_de_sport, file = "bg\ATK_S.png")
        image4 = PhotoImage(master = salle_de_sport, file = "bg\ATK_M.png")
        image5 = PhotoImage(master = salle_de_sport, file = "bg\ATK_L.png")
        Button(salle_de_sport, image = image3, command = lambda: ev_buy(idpokemon, joueur, 1, 1, 400, stats_j[6], argent, stats_poke, ev)).place(x=143,y=182)
        Button(salle_de_sport, image = image4, command = lambda: ev_buy(idpokemon, joueur, 1, 3, 1000, stats_j[6], argent, stats_poke, ev)).place(x=429,y=182)
        Button(salle_de_sport, image = image5, command = lambda: ev_buy(idpokemon, joueur, 1, 10, 1700, stats_j[6], argent, stats_poke, ev)).place(x=715,y=182)
        Label(salle_de_sport, text="Atk [1] -> 400Or").place(x=110,y=242)
        Label(salle_de_sport, text="Atk [3] -> 1000Or").place(x=396,y=242)
        Label(salle_de_sport, text="Atk [10] -> 1700Or").place(x=682,y=242)

        image6 = PhotoImage(master = salle_de_sport, file = "bg\DEF_S.png")
        image7 = PhotoImage(master = salle_de_sport, file = "bg\DEF_M.png")
        image8 = PhotoImage(master = salle_de_sport, file = "bg\DEF_L.png")
        Button(salle_de_sport, image = image6, command = lambda: ev_buy(idpokemon, joueur, 2, 1, 400, stats_j[6], argent, stats_poke, ev)).place(x=143,y=273)
        Button(salle_de_sport, image = image7, command = lambda: ev_buy(idpokemon, joueur, 2, 3, 1000, stats_j[6], argent, stats_poke, ev)).place(x=429,y=273)
        Button(salle_de_sport, image = image8, command = lambda: ev_buy(idpokemon, joueur, 2, 10, 1700, stats_j[6], argent, stats_poke, ev)).place(x=715,y=273)
        Label(salle_de_sport, text="Def [1] -> 400Or").place(x=110,y=333)
        Label(salle_de_sport, text="Def [3] -> 1000Or").place(x=396,y=333)
        Label(salle_de_sport, text="Def [10] -> 1700Or").place(x=682,y=333)

        image9 = PhotoImage(master = salle_de_sport, file = "bg\SPA_S.png")
        image10 = PhotoImage(master = salle_de_sport, file = "bg\SPA_M.png")
        image11 = PhotoImage(master = salle_de_sport, file = "bg\SPA_L.png")
        Button(salle_de_sport, image = image9, command = lambda: ev_buy(idpokemon, joueur, 3, 1, 400, stats_j[6], argent, stats_poke, ev)).place(x=143,y=364)
        Button(salle_de_sport, image = image10, command = lambda: ev_buy(idpokemon, joueur, 3, 3, 1000, stats_j[6], argent, stats_poke, ev)).place(x=429,y=364)
        Button(salle_de_sport, image = image11, command = lambda: ev_buy(idpokemon, joueur, 3, 10, 1700, stats_j[6], argent, stats_poke, ev)).place(x=715,y=364)
        Label(salle_de_sport, text="Sp_Atk [1] -> 400Or").place(x=110,y=424)
        Label(salle_de_sport, text="Sp_Atk [3] -> 1000Or").place(x=396,y=424)
        Label(salle_de_sport, text="Sp_Atk [10] -> 1700Or").place(x=682,y=424)

        image12 = PhotoImage(master = salle_de_sport, file = "bg\SPD_S.png")
        image13 = PhotoImage(master = salle_de_sport, file = "bg\SPD_M.png")
        image14 = PhotoImage(master = salle_de_sport, file = "bg\SPD_L.png")
        Button(salle_de_sport, image = image12, command = lambda: ev_buy(idpokemon, joueur, 4, 1, 400, stats_j[6], argent, stats_poke, ev)).place(x=143,y=455)
        Button(salle_de_sport, image = image13, command = lambda: ev_buy(idpokemon, joueur, 4, 3, 1000, stats_j[6], argent, stats_poke, ev)).place(x=429,y=455)
        Button(salle_de_sport, image = image14, command = lambda: ev_buy(idpokemon, joueur, 4, 10, 1700, stats_j[6], argent, stats_poke, ev)).place(x=715,y=455)
        Label(salle_de_sport, text="Sp_Def [1] -> 400Or").place(x=110,y=515)
        Label(salle_de_sport, text="Sp_def [3] -> 1000Or").place(x=396,y=515)
        Label(salle_de_sport, text="Sp_def [10] -> 1700Or").place(x=682,y=515)

        image15 = PhotoImage(master = salle_de_sport, file = "bg\SPE_S.png")
        image16 = PhotoImage(master = salle_de_sport, file = "bg\SPE_M.png")
        image17 = PhotoImage(master = salle_de_sport, file = "bg\SPE_L.png")
        Button(salle_de_sport, image = image15, command = lambda: ev_buy(idpokemon, joueur, 5, 1, 400, stats_j[6], argent, stats_poke, ev)).place(x=143,y=546)
        Button(salle_de_sport, image = image16, command = lambda: ev_buy(idpokemon, joueur, 5, 3, 1000, stats_j[6], argent, stats_poke, ev)).place(x=429,y=546)
        Button(salle_de_sport, image = image17, command = lambda: ev_buy(idpokemon, joueur, 5, 10, 1700, stats_j[6], argent, stats_poke, ev)).place(x=715,y=546)
        Label(salle_de_sport, text="Spd [1] -> 400Or").place(x=110,y=606)
        Label(salle_de_sport, text="Spd [3] -> 1000Or").place(x=396,y=606)
        Label(salle_de_sport, text="Spd [10] -> 1700Or").place(x=682,y=606)

        matthias.after(4000, lambda : matthias.destroy())
        matthias.mainloop()
        salle_de_sport.mainloop()


    #Shop
    elif id == 6:

        vendeur = Tk()
        vendeur.title("Vendeur Yoan")
        vendeur.resizable(width = False, height = False)

        Label(vendeur, text = "Bienvenue dans ma boutique! Ici vous trouverez tout ce dont un dresseur a besoin!", font = ('Arial', 10)).pack(pady=10)

        shop = Tk()
        shop.title("Boutique")
        shop.geometry("860x570")
        shop.resizable(width=False, height=False)

        image = PhotoImage(master = vendeur, file = "bg\pendeur.png")
        Label(vendeur, image = image).pack()


        info = sql_methode.info_joueur(joueur.get_id())

        argent = Label(shop, text = "Or: " + str(info[6]), font = ('Arial', 12))
        argent.place(x=400, y=20)

        pokeball = PhotoImage(master = shop, file = "bg\pokeballc.png")
        Button(shop, image = pokeball, command = lambda: buy(1, joueur.get_id(), argent)).place(x=180, y=100)
        Label(shop, text = "Pokeball  100Or", borderwidth = 5, relief = "groove").place(x=187, y = 220)
        superball = PhotoImage(master = shop, file = "bg\superballc.png")
        Button(shop, image = superball, command = lambda: buy(2, joueur.get_id(), argent)).place(x=380, y=100)
        Label(shop, text = "Superball  600Or", borderwidth = 5, relief = "groove").place(x=387, y = 220)
        hyperball = PhotoImage(master = shop, file = "bg\hyperballc.png")
        Button(shop, image = hyperball, command = lambda: buy(3, joueur.get_id(), argent)).place(x=580, y=100)
        Label(shop, text = "Hyperball  800Or", borderwidth = 5, relief = "groove").place(x=587, y = 220)

        potion = PhotoImage(master = shop, file = "bg\potionc.png")
        Button(shop, image = potion, command = lambda: buy(4, joueur.get_id(), argent)).place(x=80, y=300)
        Label(shop, text = "Potion  300Or", borderwidth = 5, relief = "groove").place(x=74, y = 384)
        superpotion = PhotoImage(master = shop, file = "bg\superpotionc.png")
        Button(shop, image = superpotion, command = lambda: buy(5, joueur.get_id(), argent)).place(x=280, y=300)
        Label(shop, text = "Superpotion  700Or", borderwidth = 5, relief = "groove").place(x=259, y = 384)
        hyperpotion = PhotoImage(master = shop, file = "bg\hyperpotionc.png")
        Button(shop, image = hyperpotion, command = lambda: buy(6, joueur.get_id(), argent)).place(x=480, y=300)
        Label(shop, text = "Hyperpotion  1 500Or", borderwidth = 5, relief = "groove").place(x=457, y = 384)
        potionmax = PhotoImage(master = shop, file = "bg\potionmaxc.png")
        Button(shop, image = potionmax, command = lambda: buy(7, joueur.get_id(), argent)).place(x=680, y=300)
        Label(shop, text = "Potion Max  2 500Or", borderwidth = 5, relief = "groove").place(x=660, y = 384)

        Button(shop, text = "Partir !", command = lambda : aurevoir(shop)).place(x=400, y=500)

        vendeur.after(4000, lambda : vendeur.destroy())
        shop.mainloop()
        vendeur.mainloop()

