import sqlite3
import sql_methode
from tkinter import *
from bouton import create
from sac import pcA, equipeA, warning

conn = sqlite3.connect('TablePokemon.db')

class Joueur():

    def __init__(self, id, mdp, pseudo, new = [False, None]):

        self.__id = id
        self.__mdp = mdp
        self.__pseudo = pseudo
        self.equipe = []
        self.pc = []

        self.init_equipe()
        self.init_pc()

        if new[0]:
            self.capture(new[1][0], new[1][1])


    def get_id(self):
        return self.__id
    def get_mdp(self):
        return self.__mdp
    def get_pseudo(self):
        return self.__pseudo


    def init_equipe(self):
        self.equipe = sql_methode.init_equipe(self.get_id())
    def get_equipe(self):
        return self.equipe
    def add_equipe(self, id):
        self.equipe.append(id)


    def init_pc(self):
        self.pc = sql_methode.init_pc(self.get_id())
    def get_pc(self):
        return self.pc
    def add_pc(self, id):
        self.pc.append(id)


    def team_free(self):
        if len(self.equipe) < 6:
           return True
        else:
             return False
    def pc_to_team(self, indice, fenetre1 = 0, fenetre2 = 0):
        if len(self.equipe) < 6:
            self.pc.remove(indice)
            self.equipe.append(indice)
            sql_methode.bascule_team_or_pc(indice, True)

            if fenetre1 != 0 and fenetre2 != 0:
                fenetre1.destroy()
                fenetre2.destroy()
                pcA(self.get_id(), self.get_pc(), self)
        else:
            warning(False)
    def team_to_pc(self, indice, fenetre1 = 0, fenetre2 = 0):
        if len(self.equipe) > 1:
            self.equipe.remove(indice)
            self.pc.append(indice)
            sql_methode.bascule_team_or_pc(indice, False)

            if fenetre1 != 0 and fenetre2 != 0:
                fenetre1.destroy()
                fenetre2.destroy()
                equipeA(self.get_id(), self.get_equipe(), self)
        else:
            warning(True)

    def capture(self, niveau, id):
        sql_methode.capture_poke(self.get_id(), id, niveau)
        self.init_pc()

        if self.team_free == True:
            for i in self.pc:
                if i == self.pc[-1]:
                    self.pc_to_team(i)

    def pokemon_in_salle(self, var):

        pokemon = Tk()
        pokemon.title("Sélection du pokémon")
        pokemon.resizable(width=False, height=False)
        pokemon["pady"] = 20
        pokemon["padx"] = 20


        pokemon_id = self.get_equipe()
        sprites = sql_methode.sprites(pokemon)
        n_pokemon_id = sql_methode.get_id_pokemon(pokemon_id)

        for i in n_pokemon_id:

            if i == n_pokemon_id[0]:
                Button(pokemon, image = sprites[i[0]], command = lambda : self.stock(pokemon_id[0], var, pokemon)).pack(pady = 10)
            elif len(n_pokemon_id) > 1:
                if i == n_pokemon_id[1]:
                    Button(pokemon, image = sprites[i[0]], command = lambda : self.stock(pokemon_id[1], var, pokemon)).pack(pady = 10)
                elif len(n_pokemon_id) > 2:
                    if i == n_pokemon_id[2]:
                        Button(pokemon, image = sprites[i[0]], command = lambda : self.stock(pokemon_id[2], var, pokemon)).pack(pady = 10)
                    elif len(n_pokemon_id) > 3:
                        if i == n_pokemon_id[3]:
                            Button(pokemon, image = sprites[i[0]], command = lambda : self.stock(pokemon_id[3], var, pokemon)).pack(pady = 10)
                        elif len(n_pokemon_id) > 4:
                            if i == n_pokemon_id[4]:
                                Button(pokemon, image = sprites[i[0]], command = lambda : self.stock(pokemon_id[4], var, pokemon)).pack(pady = 10)
                            elif len(n_pokemon_id) > 5:
                                if i == n_pokemon_id[5]:
                                    Button(pokemon, image = sprites[i[0]], command = lambda : self.stock(pokemon_id[5], var, pokemon)).pack(pady = 10)
                                elif len(n_pokemon_id) > 6:
                                    if i == n_pokemon_id[6]:
                                        Button(pokemon, image = sprites[i[0]], command = lambda : self.stock(pokemon_id[6], var, pokemon)).pack(pady = 10)


        pokemon.mainloop()
    def stock(self, id, var, pokemon):
        pokemon.destroy()
        create(var, self, id)

