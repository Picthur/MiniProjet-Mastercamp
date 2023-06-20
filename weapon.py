#Class Weapon : les différentes armes possédé par un joueur
class Weapon():
    def __init__(self, damages, usage, range):
        self.damages = damages      # Les dégats de l'arme choisi
        self.range = range          # La porté de l'arme
        self.usage = usage          # Le nombre de fois qu'on peut l'utiliser
