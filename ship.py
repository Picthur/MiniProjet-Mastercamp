
class Ship():
    nb = 0
    def __init__(self, size, row, col, direction, move):
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
    




    """ def Attacked(self, w:Weapon):
        self.health -= w.damages
        if(self.health <= 0):
            del self

    def Coordonne(self):
        coord = []
    #def movement() """