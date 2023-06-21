class Player():
    nb = 0
    def __init__(self, name):
        self.name = name        # Nom du joueur
        self.weapon = []        # Liste des armes du joueur
        self.PA = 5         # Nombre d'action du joueur
        self.ships = []          # Liste de bateau du joueur
        self.score = 0          # Score TBD
        self.base = []          # La base du joueur
        Player.nb += 1          # ID du joueur, inique
        self.id = Player.nb

    # Ajoute une arme a un joueur, si elle n'existe pas encore
    def addWeapon(self, w): 
        if w not in self.weapon:
            self.weapon.append(w)

    # Ajoute un bateau a un joueur, si elle n'existe pas encore
    def addShip(self, s):
        if s not in self.ships:
            self.ships.append(s)

    # Ajoute la base du joueur, uniquement s'il en avait pas
    def addBase(self, b):
        if self.base == []:
            self.base = b

    def set_PA (self,x):
        self.PA = x