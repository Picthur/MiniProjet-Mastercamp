import random
from ship import *
#Place le bateau sur la carte en fonction de sa direction
def placeShip(map,ship):
    match ship.direction:
        case 'E':
            placeShipEast(map,ship)
        case 'N':
            placeShipNorth(map,ship)
        case 'S':
            placeShipSouth(map,ship)
        case 'W':
            placeShipWest(map,ship)

#Les fonctions ci dessous placent un bateau sur la carte, avec b pour le point arrière, et f l'avant
def placeShipEast(map,ship):
    for i in range(ship.size):
        if(i == 0):
            map[ship.row][ship.col + i] = "b" + str(ship.id)
        elif (i == ship.size - 1):
            map[ship.row][ship.col + i] = "f" + str(ship.id)
        else:
            map[ship.row][ship.col + i] = str(ship.id) + " "

def placeShipNorth(map,ship):
    for i in range(ship.size):
        if(i == 0):
            map[ship.row - i][ship.col] = "b" + str(ship.id)
        elif (i == ship.size - 1):
            map[ship.row - i][ship.col] = "f" + str(ship.id)
        else:
            map[ship.row - i][ship.col] = str(ship.id) + " "

def placeShipSouth(map,ship):
    for i in range(ship.size):
        if(i == 0):
            map[ship.row + i][ship.col] = "b" + str(ship.id)
        elif (i == ship.size - 1):
            map[ship.row + i][ship.col] = "f" + str(ship.id)
        else:
            map[ship.row + i][ship.col] = str(ship.id) + " "

def placeShipWest(map,ship):
    for i in range(ship.size):
        if(i == 0):
            map[ship.row][ship.col - i] = "b" + str(ship.id)
        elif (i == ship.size - 1):
            map[ship.row][ship.col - i] = "f" + str(ship.id)
        else:
            map[ship.row][ship.col - i] = str(ship.id) + " "

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


#Fonction de detection de colision dans un carré de 3x3 avec pour centre une coordonnée
def willCollide(random_row, random_column, size, direction, map):

    row = random_row
    col = random_column

    for i in range (size):

        #Définition d'un carré de 3x3 avec pour centre la coordonée donnée à vérifier pour que les bateaux ne soient pas collés
        toCheck = [[row-1,col-1],[row-1,col],[row-1,col+1],      
                   [row,col-1],[row,col],[row,col+1],
                   [row+1,col-1],[row+1,col],[row+1,col+1]]
        
        #On parcourt toutes les cases à check autour du point
        for j in range(len(toCheck)):

            row_pos = toCheck[j][0]
            col_pos = toCheck[j][1]

            #Si il y a quelque chose d'autre que de l'eau (*), alors il y aura une collision
            if(map[row_pos][col_pos] != "* "):
                return True

        #On passe à la case suivante, en fonction de la direction
        match direction:
            case 'E':
                col += 1
            case 'N': 
                row -= 1
            case 'S': 
                row += 1
            case 'W':
                col -= 1

    #Sinon il n'y a pas eu de collisions
    return False

def randomShip(ship_size,map_size, map):
    
    #Création des coordonées du bateau pour pas qu'il ne soit trop au bord ou trop au milieu de la carte
    random_row = random.randint(ship_size,map_size - ship_size)
    random_column = random.randint(ship_size,round(map_size/2) - 5)

    direction = chooseDirection(random_row,map_size)

    #Si le placement générera une collision, alors on rappelle la fonction pour générer une autre position aléatoire
    #La fonction prend donc en paramètres, la position, mais également la taille, la direction, ainsi que la matrice de la map pour pouvoir vérifier
    if(willCollide(random_row, random_column, ship_size, direction, map)):
        print("COLLIDE")
        return randomShip(ship_size,map_size,map)
    
    return Ship(ship_size,random_row,random_column,direction,1)

def symmetricalShip(ship,map_size):
    
    #On recopie les attributs de l'autre bateaux, on les inverse en fonction de la map (-1 car index d'un tableau commence à 0)
    size = ship.size
    row = map_size - ship.row - 1
    col = map_size - ship.col - 1 
    
    #On inverse la direction
    match ship.direction:
        case 'E':
            direction = 'W'
        case 'N':
            direction = 'S'
        case 'S':
            direction = 'N'
            
    return Ship(size,row,col,direction,1)