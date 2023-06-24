from base import *
from ship import *
from placement import * 
from map import *
from weapon import *

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
        if s in self.ship:
            self.ship.remove(s)

    def set_PA (self,x):
        self.PA = x

    
    def initializeWeapon(self):
        w1 = Weapon(10, 10, 20)
        w2 = Weapon(2, 4, 20)
        self.addWeapon(w1)
        self.addWeapon(w2)

