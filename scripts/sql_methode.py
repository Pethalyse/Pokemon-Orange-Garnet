import sqlite3
from random import randint
from tkinter import *

conn = sqlite3.connect('TablePokemon.db')

#------------------Joueur-------------------------------

def info_joueur(id):

    """
    Récupère les informations du joueur dans l'ordre suivant:
        [pseudo, temps de jeux, nbr de connexion, nbr de combat, victoires, défaites, golds]

    arg:
        id = int
    return:
        lst
    """

    cur = conn.cursor()
    req = "select Pseudo, TempsDeJeux, NbrDeConnexion, NbrDeCombat, Victoires, Defaites, Golds from Joueur where Id = {};".format(id)
    cur.execute(req)

    a = cur.fetchall()[0]

    conn.commit()
    cur.close()

    return a

def init_equipe(id):

    """
    Récupère l'Id des pokemon capturé et dans l'équipe du joueur dans une liste

    arg:
        id = int
    return:
        equipe = lst
    """

    cur = conn.cursor()
    req = "select Id from PokemonJoueur where TeamPoke = True and IdJoueur = {};".format(id)
    cur.execute(req)

    equipe = []

    for i in cur.fetchall():
        equipe.append(i[0])

    conn.commit()
    cur.close()

    return equipe

def init_pc(id):

    """
    Récupère les pokemon capturé et dans le pc du joueur

    arg:
        id = int
    return:
        pc = lst
    """

    cur = conn.cursor()
    req = "select Id from PokemonJoueur where TeamPoke = False and IdJoueur = {};".format(id)
    cur.execute(req)

    pc = []

    for i in cur.fetchall():
        pc.append(i[0])

    conn.commit()
    cur.close()

    return pc

def get_objet(id, nom, typ):

    cur = conn.cursor()
    req = "insert into Shop (IdJoueur, Nom, Type) values ({}, '{}', '{}')".format(id, nom, typ)
    cur.execute(req)

    conn.commit()
    cur.close()

def update_golds(id, somme):

    cur = conn.cursor()
    req = "update Joueur set golds = golds + {} where Id = {}".format(somme, id)
    cur.execute(req)

    conn.commit()
    cur.close()

def get_nbr_items(id):

    item = {}

    cur = conn.cursor()
    req = "select count(*) from shop where idJoueur = {} and Nom = 'Pokeball'".format(id)
    cur.execute(req)
    item["pokeball"] = cur.fetchall()[0][0]

    cur = conn.cursor()
    req = "select count(*) from shop where idJoueur = {} and Nom = 'SuperBall'".format(id)
    cur.execute(req)
    item["superball"] = cur.fetchall()[0][0]

    cur = conn.cursor()
    req = "select count(*) from shop where idJoueur = {} and Nom = 'HyperBall'".format(id)
    cur.execute(req)
    item["hyperball"] = cur.fetchall()[0][0]

    cur = conn.cursor()
    req = "select count(*) from shop where idJoueur = {} and Nom = 'Potion'".format(id)
    cur.execute(req)
    item["potion"] = cur.fetchall()[0][0]

    cur = conn.cursor()
    req = "select count(*) from shop where idJoueur = {} and Nom = 'Super Potion'".format(id)
    cur.execute(req)
    item["superpotion"] = cur.fetchall()[0][0]

    cur = conn.cursor()
    req = "select count(*) from shop where idJoueur = {} and Nom = 'Hyper Potion'".format(id)
    cur.execute(req)
    item["hyperpotion"] = cur.fetchall()[0][0]

    cur = conn.cursor()
    req = "select count(*) from shop where idJoueur = {} and Nom = 'Potion Max'".format(id)
    cur.execute(req)
    item["potionmax"] = cur.fetchall()[0][0]

    conn.commit()
    cur.close()

    return item
#------------------PokemonJoueur-------------------------------

def capture_poke(idJoueur, idPokemon, niveau):
    """
    Modifie la table PokemonJoueur et y ajoute le pokemon capturé

    arg:
        idJoueur : int
        statsPokemon : dict
    """

    statsPokemon = get_stats_poke_non_joueur(idPokemon, niveau)

    cur = conn.cursor()
    req = "insert into PokemonJoueur (IdJoueur, IdPokemon, NiveauPoke, Talent, CurrentHp, HP, ATK, DEF, SP_ATK, SP_DEF, SPD, TeamPoke, rencontre, ev)"
    req += " Values ({}, {}, {}, '{}'".format(idJoueur, statsPokemon["id"], statsPokemon["niveau"], statsPokemon["talent"])
    req += ", {}, {}, {}, {}, {}, {}, {}, False, False, 100)".format(statsPokemon["hp"], statsPokemon["hp"],statsPokemon["atk"],statsPokemon["def"],
                                                                              statsPokemon["sp_atk"],statsPokemon["sp_def"],statsPokemon["spd"])

    cur.execute(req)
    conn.commit()
    cur.close()

def get_stat_poke_joueur(id):

    """
    Récupère les stats du pokemon entré en id de la table PokemonJoueur

    arg:
        id = int
    return:
        dict
    """
    cur = conn.cursor()
    req = "select NiveauPoke, Hp, ATK, DEF, SP_ATK, SP_DEF, SPD, Talent, CurrentHp, TeamPoke, Ev, idjoueur from PokemonJoueur where Id = {};".format(id)
    cur.execute(req)

    a = cur.fetchall()[0]
    b = {}

    for i in range(len(a)):
        if i == 0:
            b["niveau"] = a[i]
        if i == 1:
            b["hp"] = a[i]
        if i == 2:
            b["atk"] = a[i]
        if i == 3:
            b["def"] = a[i]
        if i == 4:
            b["sp_atk"] = a[i]
        if i == 5:
            b["sp_def"] = a[i]
        if i == 6:
            b["spd"] = a[i]
        if i == 7:
            b["talent"] = a[i]
        if i == 8:
            b["current_hp"] = a[i]
        if i == 9:
            b["teampoke"] = a[i]
        if i == 10:
            b["ev"] = a[i]
        if i == 11:
            b["idjoueur"] = a[i]

    req = "select IdPokemon from PokemonJoueur where id = {}".format(id)
    cur.execute(req)

    req = "select POKEMON.NAME, POKEMON.TYPE1, POKEMON.TYPE2 from PokemonJoueur Join POKEMON On PokemonJoueur.IdPokemon = POKEMON.NUMBER"
    req += " Where PokemonJoueur.IdPokemon = {} and POKEMON.CODE = 1".format(cur.fetchall()[0][0])
    cur.execute(req)

    r = cur.fetchall()
    b["nom"] = r[0][0]
    b["types"] = [r[0][1],r[0][2]]

    conn.commit()
    cur.close()

    return b

def modif_stat_poke(id, nom_stat, combien = 0):

    stats = get_stat_poke_joueur(id)
    cur = conn.cursor()

    if nom_stat == "current_hp":
        if combien > 0:
            if combien > stats["hp"]:
                combien = 0
                while stats["current_hp"] + combien < stats["hp"]:
                    combien+=1

        if stats["current_hp"] + combien < 0:
            while stats["current_hp"] + combien < 0:
                combien+=1

        req = "update PokemonJoueur set CurrentHp = currenthp + {} where id = {}".format(combien, id)
        cur.execute(req)

    elif nom_stat == "rencontre":
        req = "Update PokemonJoueur set Rencontre = {} where id = {}".format(combien, id)
        cur.execute(req)

    elif type(nom_stat) == int:

        if nom_stat == 0:
            req = "Update PokemonJoueur set Hp = Hp + {} , CurrentHp = CurrentHp + {} , ev = ev - {} where id = {}".format(combien, combien, combien, id)
            cur.execute(req)
        elif nom_stat == 1:
            req = "Update PokemonJoueur set Atk = Atk + {} , ev = ev - {} where id = {}".format(combien, combien, id)
            cur.execute(req)
        elif nom_stat == 2:
            req = "Update PokemonJoueur set def = def + {} , ev = ev - {} where id = {}".format(combien, combien, id)
            cur.execute(req)
        elif nom_stat == 3:
            req = "Update PokemonJoueur set sp_Atk = sp_Atk + {} , ev = ev - {} where id = {}".format(combien, combien, id)
            cur.execute(req)
        elif nom_stat == 4:
            req = "Update PokemonJoueur set sp_def = sp_def + {} , ev = ev - {} where id = {}".format(combien, combien, id)
            cur.execute(req)
        elif nom_stat == 5:
            req = "Update PokemonJoueur set spd = spd + {} , ev = ev - {} where id = {}".format(combien, combien, id)
            cur.execute(req)


    conn.commit()
    cur.close()

def bascule_team_or_pc(id, bool):
    """
    Bascule dans la base de donné TeamPoke de la table PokemonJoueur à True ou False

    arg:
        id = int
        bool = booleen
    """

    cur = conn.cursor()

    if bool is True:
        req = "update PokemonJoueur set TeamPoke = True where id = {}".format(id)
    elif bool is False:
        req = "update PokemonJoueur set TeamPoke = False where id = {}".format(id)

    cur.execute(req)
    conn.commit()
    cur.close()

def set_level_up(id):
    """
    Monte le niveau du pokemon de 1 et change les stats

    arg:
        id = int
    """

    cur = conn.cursor()

    req = "update PokemonJoueur set NiveauPoke = NiveauPoke+1 where id = {};".format(id)
    cur.execute(req)

    cur.execute("select NiveauPoke, IdPokemon from PokemonJoueur where id = {};".format(id))

    for i in cur.fetchall():

        niveau = i[0]
        a = base_stat(i[1], 1)


    req = "update PokemonJoueur set (HP, ATK, DEF, SP_ATK, SP_DEF, SPD) = ({}, {}, {}, {}, {}, {}) where id = {};".format(
                                                round((2*a["hp"]*niveau/100) + niveau + 10), round((2*a["atk"]*niveau/100) + 5),
                                                round((2*a["def"]*niveau/100) + 5),round((2*a["sp_atk"]*niveau/100) + 5),
                                                round((2*a["sp_def"]*niveau/100) + 5),round((2*a["spd"]*niveau/100) + 5), id)

    cur.execute(req)
    conn.commit()
    cur.close()

def base_stat(id, code):
    """
    Récupère les bases statistique d'un pokemon

        arg:
            id = int
            code = int (1/2/3)
        return:
            dict
    """

    cur = conn.cursor()
    req = "select HP, ATK, DEF, SP_ATK, SP_DEF, SPD"
    req += " from Pokemon where NUMBER = {} and Code = {};".format(id, code)
    cur.execute(req)

    a = cur.fetchall()[0]
    b = {}

    for i in range(len(a)):
        if i == 0:
            b["hp"] = a[i]
        elif i == 1:
            b["atk"] = a[i]
        elif i == 2:
            b["def"] = a[i]
        elif i == 3:
            b["sp_atk"] = a[i]
        elif i == 4:
            b["sp_def"] = a[i]
        elif i == 5:
            b["spd"] = a[i]

    return b

def get_id_pokemon(pokemon):

    pokemons = pokemon

    cur = conn.cursor()
    stock = []
    for i in pokemons:
        req = "select idPokemon from PokemonJoueur where id == {}".format(i)
        cur.execute(req)
        stock.append(cur.fetchall()[0])

    conn.commit()
    cur.close()

    return stock

def poke_rencontre(bool = True, id = 0):

    if bool == True:
        cur = conn.cursor()
        req = "select id from PokemonJoueur where Rencontre = True"
        cur.execute(req)

        stock = cur.fetchall()

    elif bool == False:
        cur = conn.cursor()
        req = "select id from PokemonJoueur where Rencontre = True and idJoueur not in ({})".format(id)
        cur.execute(req)

        stock = cur.fetchall()

    conn.commit()
    cur.close()

    return stock

def get_id_joueur(id):

        joueur = []
        cur = conn.cursor()
        req = "select idJoueur from PokemonJoueur where id = {}".format(id)
        cur.execute(req)
        joueur.append(cur.fetchall()[0][0])

        req = "select Joueur.Pseudo from PokemonJoueur join Joueur on PokemonJoueur.idJoueur = Joueur.id where PokemonJoueur.id = {}".format(id)
        cur.execute(req)
        joueur.append(cur.fetchall()[0][0])

        conn.commit()
        cur.close()

        return joueur

def get_affinite(idpokemon1, idpokemon2):

        cur = conn.cursor()
        req = "select Pourcent, nbractions from Affinites where IdPokemon1 in ({}, {}) and IdPokemon2 in ({}, {})".format(idpokemon1, idpokemon2, idpokemon1, idpokemon2)
        cur.execute(req)

        return cur.fetchall()

        conn.commit()
        cur.close()
def new_affinite(idpokemon1, idpokemon2):

    cur = conn.cursor()
    req = "Insert into Affinites values ({}, {}, 0, 10)".format(idpokemon1, idpokemon2)
    cur.execute(req)

    conn.commit()
    cur.close()
def modif_affinite(idpokemon1, idpokemon2, pourcent, cout):

    cur = conn.cursor()
    req = "update Affinites set pourcent = pourcent + {} where idpokemon1 in ({}, {}) and idpokemon2 in ({}, {})".format(pourcent, idpokemon1, idpokemon2, idpokemon1, idpokemon2)
    cur.execute(req)

    req = "update Affinites set nbractions = nbractions + {} where idpokemon1 in ({}, {}) and idpokemon2 in ({}, {})".format(cout, idpokemon1, idpokemon2, idpokemon1, idpokemon2)
    cur.execute(req)

    conn.commit()
    cur.close()

def cantine_insert(id, stat, combien):

        cur = conn.cursor()
        req = "insert into cantine values ({}, {}, {}, 5)".format(id, stat, combien)
        cur.execute(req)

        conn.commit()
        cur.close()
def cantine_get(id):

        cur = conn.cursor()
        req = "select * from cantine where idpokemon = {}".format(id)
        cur.execute(req)

        return cur.fetchall()

        conn.commit()
        cur.close()
#------------------PokemonSauvage-------------------------------

def get_stats_poke_non_joueur(number, niveau):
    """
    Récupère les stats d'un pokemon qui n'est pas à un joueur de la table POKEMON

        arg:
            number = int
            niveau = int
        return:
            dict
    """

    cur = conn.cursor()
    req = "select Name, Type1, Type2, ABILITY1, ABILITY2, ABILITY_HIDDEN, HP, ATK, DEF, SP_ATK, SP_DEF, SPD"
    req += " from Pokemon where NUMBER = {} and MEGA_EVOLUTION = 0;".format(number)
    cur.execute(req)

    a = cur.fetchall()[0]
    b = {}

    for i in range(len(a)):
        if i == 0:
            b["nom"] = a[i]
        elif i == 1:
            b["types"] = [a[i]]
        elif i == 2:
            b["types"].append(a[i])
        elif i == 3:
            b["talent"] = [a[i]]
        elif i == 4:
            b["talent"].append(a[i])
        elif i == 5:
            b["talent"].append(a[i])
        elif i == 6:
            b["hp"] = round((2*a[i]*niveau/100) + niveau + 10)
        elif i == 7:
            b["atk"] = round((2*a[i]*niveau/100) + 5)
        elif i == 8:
            b["def"] = round((2*a[i]*niveau/100) + 5)
        elif i == 9:
            b["sp_atk"] = round((2*a[i]*niveau/100) + 5)
        elif i == 10:
            b["sp_def"] = round((2*a[i]*niveau/100) + 5)
        elif i == 11:
            b["spd"] = round((2*a[i]*niveau/100) + 5)


    c = b["talent"]
    b["talent"] = b["talent"][randint(0,2)]

    while type(b["talent"]) is not str:
        b["talent"] = c[randint(0,2)]

    b["id"] = number
    b["niveau"] = niveau

    conn.commit()
    cur.close()

    return b

#---------------------Sprites-----------------------------------

def sprites(root):

    const = "{}.png"
    sprites = {}

    cur = conn.cursor()
    req = "select NUMBER, NAME, CODE from Pokemon where CODE = 1;"
    cur.execute(req)

    for i in cur.fetchall():
        sprites[i[0]] = PhotoImage(master = root, file="sprites\{}.png".format(i[1]).replace(" ","-").replace("'","").replace(":","").replace("Mr.Rime","Mr-Rime").replace("Mr.Mime","Mr-Mime").replace("Mime-Jr.","Mime-Jr"))

    conn.commit()
    cur.close()


    return sprites

