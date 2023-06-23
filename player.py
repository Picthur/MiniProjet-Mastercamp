from base import *
from ship import *
from placement import * 
from map import *
from weapon import *

#Class Weapon : les différentes armes possédé par un joueur
class Weapon():
    def __init__(self, damages, usage, range):
        self.damages = damages      # Les dégats de l'arme choisi
        self.range = range          # La porté de l'arme
        self.usage = usage          # Le nombre de fois qu'on peut l'utiliser


# Class Bateau : les différents bateaux possédé par un joueur
class Ship():
    nb = 0
    def __init__(self, size, row, col, direction, move,):
        self.size = size        # Taille du bateau 
        self.row = row         # Position x du bateau
        self.col = col         # Position y du bateau
        self.direction = direction          # Orientation du Bateau (N S O E)
        self.health = size      # PV Actuelle du bateau (basé initialement sur la taille du bateau)
        self.maxhealth = size   # PV Maximal/Initial du bateau 
        self.move = move        # Combien 
        Ship.nb += 1            # On incrémente le nombre de bateaux
        self.id = Ship.nb       # Id correspond au ieme bateau créé

    def get_id(self):
        return self.id



# Class joueur: 
class Player():
    id = 0
    def __init__(self, name):
        self.name = name        # Nom du joueur
        self.weapon = []        # Liste des armes du joueur
        self.action = 5         # Nombre d'action du joueur
        self.ship = []          # Liste de bateau du joueur
        self.score = 0          # Score TBD
        self.base = []          # La base du joueur
        Player.id += 1          # ID du joueur, inique

    def get_id(self):
        return self.id
    
    # Ajoute une arme a un joueur, si elle n'existe pas encore
    def addWeapon(self, w: Weapon): 
        if w not in self.weapon:
            self.weapon.append(w)

    # Ajoute un bateau a un joueur, si elle n'existe pas encore
    def addShip(self, s: Ship):
        if s not in self.ship:
            self.ship.append(s)

    # Ajoute la base du joueur, uniquement s'il en avait pas
    def addBase(self, b:Base):
        if self.base == []:
            self.base = b
    
    def removeShip(self, s: Ship):
        self.ship.remove(s)





