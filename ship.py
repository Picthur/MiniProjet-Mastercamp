from weapon import *

class Ship():
    nb = 0
    def __init__(self, size, row, col, direction, movement):
        self.size = size        # Taille du bateau 
        self.row = row         # ligne du bateau
        self.col = col         # colonne du bateau
        self.direction = direction          # Orientation du Bateau (N S O E)
        self.health = size      # PV Actuelle du bateau (basé initialement sur la taille du bateau)
        self.maxhealth = size   # PV Maximal/Initial du bateau 
        self.movementment = movement        # Combien 
        Ship.nb += 1            # On incrémente le nombre de bateaux
        self.id = Ship.nb       # Id correspond au ieme bateau créé

    def get_id(self):
        return self.id