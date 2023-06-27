
#Fonction de detection de colision dans un carré de 3x3 avec pour centre une coordonnée
def willCollideOnPlacement(random_row, random_column, size, direction, map):

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

#Vérifie si en se déplacant vers l'avant il y aura une collision
def willCollideForward(ship, map, opponentBase):

    #Vu que la coordonée de base du bateau est à l'arrière, on se déplace jusqu'à l'avant
    (row,col) = goToFront(ship)

    movement = ship.movement
    direction = ship.direction

    #ensuite, pour le nombre de case qu'est censé se déplacer le bateau, on vérifie s'il y a autre chose que de l'eau
    for i in range (movement):

        match direction:
            case 'E':
                col += 1
            case 'N': 
                row -= 1
            case 'S': 
                row += 1
            case 'W':
                col -= 1

        #Si on dépasse la taille de la carte, collision
        if((col < 0 or col > (map.size - 1)) or (row < 0 or row > (map.size -1))):
            return True
        #Si il y a quelque chose d'autre que de l'eau (*), alors il y aura une collision
        if(map.matrix[row][col] != "* " and map.matrix[row][col] != opponentBase):
            return True
        
    return False

def willCollideBackward(ship, map, opponentBase):

    row = ship.row
    col = ship.col
    movement = ship.movement
    direction = ship.direction

    for i in range (movement):

        #On check la case devant
        match direction:
            case 'E':
                col -= 1
            case 'N': 
                row += 1
            case 'S': 
                row -= 1
            case 'W':
                col += 1

        
        #Si on dépasse la taille de la carte, collision
        if((col < 0 or col > (map.size - 1)) or (row < 0 or row > (map.size -1))):
            return True
        
        #Si il y a quelque chose d'autre que de l'eau (*) ou la base adverse, alors il y aura une collision
        if(map.matrix[row][col] != "* " and map.matrix[row][col] != opponentBase):
            return True
        
    return False


#Pour un déplacement vers l'avant, le point de départ est l'arrière du bateau, il faut se déplacer à l'avant
def goToFront(ship):

    row = ship.row
    col = ship.col
    size = ship.size
    direction = ship.direction

    #Si le bateau fait 3 de longueur et qu'on est sur l'arrière, il faut avancer de 3 - 1 = 2
    for i in range (size - 1):
        match direction:
            case 'E':
                col += 1
            case 'N': 
                row -= 1
            case 'S': 
                row += 1
            case 'W':
                col -= 1
    #Renvoi de la position de départ pour avancer
    return (row,col)  

def willCollideRotation(ship,nextShipDirection,map, opponentBase):

    row = ship.row
    col = ship.col
    size = ship.size

    #Pivot autour du back du bateau donc si longueur de trois vers Est et rotation à gauche, check 3 - 1 = 2 case au dessus du back
    for i in range (size - 1):
        #On check la case devant
        match nextShipDirection:
            case 'E':
                col += 1
            case 'N': 
                row -= 1
            case 'S': 
                row += 1
            case 'W':
                col -= 1
                    
        #Si on dépasse la taille de la carte, collision
        if((col < 0 or col > (map.size - 1)) or (row < 0 or row > (map.size -1))):
            return True
        
        #Si il y a quelque chose d'autre que de l'eau (*) ou la base adverse, alors il y aura une collision
        if(map.matrix[row][col] != "* " and map.matrix[row][col] != opponentBase):
            return True
        
    return False