from Classbase import *
from ClassShip import *
from placement import * 
from ClassPlayer import *
import random


class Map: 
    #Definition de la taille des bases
    BASE_HEIGHT = 5 
    BASE_LENGTH = 4

    #Definition de la taille de la carte
    def __init__(self, size):
        self.size = size
        self.bases = []
        self.ships = []

    #Creation de la matrice correspondant à la carte
    def createMap(self):
        self.matrix = [["* "] * self.size for i in range (self.size)]
    
    #Affichage de la carte
    def displayMap(self):
        for row in self.matrix:
            print(' '.join(row))
        print()

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
                self.matrix[start_pos_B1][j] = b1.base[i][j]
            start_pos_B1 += 1

        #Symétrique par rapport à la B1
        start_pos_B2 = self.size - (base_random_pos) - self.BASE_HEIGHT

        #Ajout de la base 2 à la carte, de manière symétrique
        for i in range (len(b2.base)):
            for j in range(len(b2.base[0])):

                self.matrix[start_pos_B2][self.size - 1 - j] = b2.base[i][j]
            start_pos_B2 += 1
    
    def initializeShips(self):

        #On place des bateaux de taille 2,3,4,5
        for i in range (2,6):
            
            #Création d'un bateau de coordonées et de direction aléatoire
            s1 = randomShip(i,self.size,self.matrix)
            self.ships.append(s1)

            #Placé selon sa direction
            placeShip(s1, self.matrix)
        
        #On va recopier le nombre de bateaux présents
        ship_number = len(self.ships)
        for j in range (ship_number):
            
            #On créer les bateaux symétriques
            s2 = symmetricalShip(self.ships[j],self.size)
            self.ships.append(s2)

            #On les place
            placeShip(s2, self.matrix)

    def removeShipMap(self, s: Ship):
        self.ships.remove(s)

        