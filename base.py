class Base:
    #Tableau de longueur hauteur correspondant à la taille d'une base
    def __init__(self, name, height, length):
        self.base = [[name]*length for i in range(height)]

    #Fonction d'affichage test
    def displayBase(self):  
        for i in range (len(self.base)):
            print(self.base[i])

