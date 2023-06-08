import pygame

pygame.init()

class Base:
    def __init__(self, name):
        self.base = [[name]*4 for i in range(5)]

    def displayBase(self):  
        for i in range (len(self.base)):
            print(self.base[i])

#Class Weapon : les différentes armes possédé par un joueur
class Weapon():
    def __init__(self, name, damages, usage, range):
        self.name = name            # Le nom de l'arme
        self.damages = damages      # Les dégats de l'arme choisi
        self.range = range          # La porté de l'arme
        self.usage = usage          # Le nombre de fois qu'on peut l'utiliser


# Class Bateau : les différents bateaux possédé par un joueur
class Ship():
    id = 0
    def __init__(self, name, size, pos_x, pos_y, way, move,):
        self.name = name        # Nom du bateau
        self.size = size        # Taille du bateau 
        self.position = [pos_x,pos_y]   # Coordonnée X Y du point de base du bateau
        self.way = way          # Orientation du Bateau (N S O E)
        self.health = size      # PV Actuelle du bateau (basé initialement sur la taille du bateau)
        self.maxhealth = size   # PV Maximal/Initial du bateau 
        self.move = move        # Combien de mouvement le bateau peut faire par tours
        Ship.id += 1            # ID du bateau qui s'incrémente lors de la création

    # Fonction pour faire baisser les PV du bateau attaqué en fonction des degats de l'arme attaquante
    # Si le bateau a plus de PV, il est détruit et enlever des class Player
    def Attacked(self, w:Weapon):
        self.health -= w.damages
        if(self.health <= 0):
            del self

    #TODO
    def Coordonne(self):
        coord = []
    #def movement()

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

    # Ajoute une arme a un joueur, si elle n'existe pas encore
    def addWeapon(self, w: Weapon): 
        if w not in self.weapon:
            self.weapon.append(w)

    # Ajoute un bateau a un joueur, si elle n'existe pas encore
    def addShip(self, s: Ship):
        if s not in self.ship:
            self.ship.append(s)

    # Ajoute la base du joueur, uniquement si il en avait pas
    def addBase(self, b:Base):
        if self.base == []:
            self.base = b

    

p1 = Player("p1")
s1 = Ship("b1", 3, 5, 5, "N", 3, 2)
p1.addShip(s1)

print(p1.ship[0].size)
print(p1.__str__)
