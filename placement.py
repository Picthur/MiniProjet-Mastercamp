import random
from ship import *
from collide import *

#Place le bateau sur la carte en fonction de sa direction
def placeShip(ship,matrix):
    match ship.direction:
        case 'E':
            placeShipEast(ship,matrix)
        case 'N':
            placeShipNorth(ship,matrix)
        case 'S':
            placeShipSouth(ship,matrix)
        case 'W':
            placeShipWest(ship,matrix)

#Les fonctions ci dessous placent un bateau sur la carte, avec b pour le point arrière, et f l'avant
def placeShipEast(ship,matrix):
    for i in range(ship.size):
        if(i == 0):
            matrix[ship.row][ship.col + i] = "b" + str(ship.id)
        elif (i == ship.size - 1):
            matrix[ship.row][ship.col + i] = "f" + str(ship.id)
        else:
            matrix[ship.row][ship.col + i] = str(ship.id) + " "

def placeShipNorth(ship,matrix):
    for i in range(ship.size):
        if(i == 0):
            matrix[ship.row - i][ship.col] = "b" + str(ship.id)
        elif (i == ship.size - 1):
            matrix[ship.row - i][ship.col] = "f" + str(ship.id)
        else:
            matrix[ship.row - i][ship.col] = str(ship.id) + " "

def placeShipSouth(ship,matrix):
    for i in range(ship.size):
        if(i == 0):
            matrix[ship.row + i][ship.col] = "b" + str(ship.id)
        elif (i == ship.size - 1):
            matrix[ship.row + i][ship.col] = "f" + str(ship.id)
        else:
            matrix[ship.row + i][ship.col] = str(ship.id) + " "

def placeShipWest(ship,matrix):
    for i in range(ship.size):
        if(i == 0):
            matrix[ship.row][ship.col - i] = "b" + str(ship.id)
        elif (i == ship.size - 1):
            matrix[ship.row][ship.col - i] = "f" + str(ship.id)
        else:
            matrix[ship.row][ship.col - i] = str(ship.id) + " "

#Choisit aléatoirement une direction pour un bateau
def chooseDirection(random_row, map_size):

    #On choisit la direction du bateau aléatoirement entre E et Nord/Sud
    coinToss = random.randint(0,1)
    
    if(coinToss == 0):
        return 'E'
    else:
        if(random_row > map_size/2): #Si la ligne aléatoire est dans la partie sud (supérieure à la moitié de la taille de la carte) alors on pointe vers le nord, sinon l'inverse
            return 'N'
        else:
            return 'S'


def randomShip(ship_size,map_size, map):
    
    #Création des coordonées du bateau pour pas qu'il ne soit trop au bord ou trop au milieu de la carte
    random_row = random.randint(ship_size,map_size - ship_size)
    random_column = random.randint(ship_size,round(map_size/2) - 5)

    direction = chooseDirection(random_row,map_size)

    #Si le placement générera une collision, alors on rappelle la fonction pour générer une autre position aléatoire
    #La fonction prend donc en paramètres, la position, mais également la taille, la direction, ainsi que la matrice de la map pour pouvoir vérifier
    if(willCollideOnPlacement(random_row, random_column, ship_size, direction, map)):
        return randomShip(ship_size,map_size,map)
    
    #Donne une capacité de mouvement en fonction de la taille, + c'est gros, - ça se déplace vite
    movement = defineMovementBySize(ship_size)
    return Ship(ship_size,random_row,random_column,direction,movement)



def symmetricalShip(ship,map_size):
    
    #On recopie les attributs de l'autre bateaux, on les inverse en fonction de la map (-1 car index d'un tableau commence à 0)
    size = ship.size
    row = map_size - ship.row - 1
    col = map_size - ship.col - 1
    movement = ship.movement
    
    #On inverse la direction
    match ship.direction:
        case 'E':
            direction = 'W'
        case 'N':
            direction = 'S'
        case 'S':
            direction = 'N'
            
    return Ship(size,row,col,direction,movement)


        
#Les fonctions ci dessous effacent un bateau sur la carte, remplacant par * 
def eraseShipEast(ship,matrix):
    for i in range(ship.size):
        matrix[ship.row][ship.col + i] = "* "

def eraseShipNorth(ship,matrix):
    for i in range(ship.size):
        matrix[ship.row - i][ship.col] = "* "

def eraseShipSouth(ship,matrix):
    for i in range(ship.size):
        matrix[ship.row + i][ship.col] = "* "

def eraseShipWest(ship,matrix):
    for i in range(ship.size):
        matrix[ship.row][ship.col - i] = "* "

def eraseShip(ship,matrix):
    match ship.direction:
        case 'E':
            eraseShipEast(ship,matrix)
        case 'N':
            eraseShipNorth(ship,matrix)
        case 'S':
            eraseShipSouth(ship,matrix)
        case 'W':
            eraseShipWest(ship,matrix)


 #retourne la vitesse que doit avoir le bateau selon sa taille
def defineMovementBySize(size):
    match size:
        case 2:
            return 4
        case 3:
            return 3
        case 4:
            return 2
        case 5:
            return 2
        
#Permet de faire avancer le bateau vers l'avant
def moveShipForward(ship,map):

    row = ship.row
    col = ship.col
    movement = ship.movement
    direction = ship.direction

    #On efface la position actuelle du bateau
    eraseShip(ship,map.matrix)

    #Déplacement du nombre de case correspondant à sa vitesse
    for i in range (movement):

        #Récupération de la direction
        match direction:
            case 'E':
                col += 1
            case 'N': 
                row -= 1
            case 'S': 
                row += 1
            case 'W':
                col -= 1
        
        ship.set_row(row)
        ship.set_col(col)

    #Placement du bateau au bon endroit
    placeShip(ship,map.matrix)

#Même fonction qu'au dessus
def moveShipBackward(ship,map):

    row = ship.row
    col = ship.col
    movement = ship.movement
    direction = ship.direction

    eraseShip(ship,map.matrix)

    for i in range (movement):

        match direction:
            case 'E':
                col -= 1
            case 'N': 
                row += 1
            case 'S': 
                row -= 1
            case 'W':
                col += 1
        
        ship.set_row(row)
        ship.set_col(col)

    placeShip(ship,map.matrix)

     
def rotateShipLeft(ship):

    direction = ship.direction

    match direction:
        case 'N':
            return 'W'
        case 'W':
            return 'S'
        case 'S':
            return 'E'
        case 'E':
            return 'N'
        
def rotateShipRight(ship):

    direction = ship.direction

    match direction:
        case 'N':
            return 'E'
        case 'E':
            return 'S'
        case 'S':
            return 'W'
        case 'W':
            return 'N'


