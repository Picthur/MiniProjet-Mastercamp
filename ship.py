class Ship():
    id = 0
    def __init__(self, name, size, pos_x, pos_y, way, move,):
        self.name = name        # Nom du bateau
        self.size = size        # Taille du bateau 
        self.position = [pos_x,pos_y]   # Coordonnée X Y du point de base du bateau
        self.way = way          # Orientation du Bateau (N S O E)
        self.health = size      # PV Actuelle du bateau (basé initialement sur la taille du bateau)
        self.maxhealth = size   # PV Maximal/Initial du bateau 
        self.move = move        # Combien 
        Ship.id += 1

    def Attacked(self, w:Weapon):
        self.health -= w.damages
        if(self.health <= 0):
            del self

    def Coordonne(self):
        coord = []
    #def movement()