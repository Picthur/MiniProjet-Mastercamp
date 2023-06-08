from base import *
import random

class Map: 
    #Definition de la taille des bases
    BASE_HEIGHT = 5 
    BASE_LENGTH = 4

    #Definition de la taille de la carte
    def __init__(self, size):
        self.size = size
        self.bases = []

    #Creation de la matrice correspondant à la carte
    def createMap(self):
        self.map = [["* "] * self.size for i in range (self.size)]
    
    #Affichage de la carte
    def displayMap(self):
        for row in self.map:
            print(' '.join(row))

    #Creation des bases de manière aléatoire
    def initializeBase(self):
        b1 = Base('B1', self.BASE_HEIGHT,self.BASE_LENGTH)
        b2 = Base('B2', self.BASE_HEIGHT,self.BASE_LENGTH)

        self.bases.append(b1)
        self.bases.append(b2)
        
        #position y de la première base
        base_random_pos = random.randint(0,self.size - self.BASE_HEIGHT - 1)
        start_pos_B1 = base_random_pos 
        
        #On va à la position donnée et on ajoute 1 à 1 la base à la carte 
        for i in range (len(b1.base)):
            for j in range(len(b1.base[0])):
                self.map[start_pos_B1][j] = b1.base[i][j]
            start_pos_B1 += 1

        #Symétrique par rapport à la B1
        start_pos_B2 = self.size - (base_random_pos) - self.BASE_HEIGHT

        #Ajout de la base 2 à la carte, de manière symétrique
        for i in range (len(b2.base)):
            for j in range(len(b2.base[0])):

                self.map[start_pos_B2][self.size - 1 - j] = b2.base[i][j]
            start_pos_B2 += 1


        

m1 = Map(31)
m1.createMap()
m1.initializeBase()
m1.displayMap()




