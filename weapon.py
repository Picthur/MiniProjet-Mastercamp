#Class Weapon : les différentes armes possédé par un joueur
class Weapon():
    nb = 0
    def __init__(self, damages, usage, range):
        self.damages = damages      # Les dégats de l'arme choisi
        self.range = range          # La porté de l'arme
        self.usage = usage         # Le nombre de fois qu'on peut l'utiliser
        Weapon.nb += 1            # On incrémente le nombre de bateaux
        self.id = Weapon.nb

