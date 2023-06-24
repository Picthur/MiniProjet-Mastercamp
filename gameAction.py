from collide import *
from placement import *
from map import *
from player import *
from game import *

#Défini qui joue en fonction du nombre de tour
def whoPlays(turn,p1,p2):
    if(turn %2 == 0):
        return p1, p2
    else:
        return p2, p1

def selectShip(map, player):
        
    #A chaque tour défini les bateaux encore "vivants" du joueur
    aliveShips = []
    for ship in player.ship:
        aliveShips.append(str(ship.id))
        
    #Choix du bateau que le joueur veut prendre
    choice = input("Choisir un bateau (id)\n")
        
    if(choice not in aliveShips):
        print("Ce n'est pas un de tes bateaux")
    else:
        #Selection du bateau
        ship = map.ships[int(choice) - 1]
        return ship
    

def selectWeapon(player):
        
    #A chaque tour défini les bateaux encore "vivants" du joueur
    aliveWeapon = []
    for weapon in player.weapon:
        aliveWeapon.append(str(weapon.id))
        
    #Choix du bateau que le joueur veut prendre
    print(aliveWeapon)
    choice = input("Choisir une arme (id)\n")
        
    if(choice not in aliveWeapon):
        print("Ce n'est pas une arme valable")
    else:
        #Selection d'une arme
        weapon = player.weapon[int(choice) - 1]
        return weapon
    

def selectWay(): 
    choice = input("Choisir une direction de tir : 'N', 'S', 'E', 'O'\n")
    return choice


def moveShip(map, player):

    #Permet au joueur de selectionner le bateau qu'il veut jouer en fonction de son ID
    ship = selectShip(map, player)

    #Choix de la direction par l'utilisateur
    directionChoice = input("Avancer ou Reculer ?\n")

    #Choix d'avancer ou de reculer
    if(directionChoice == "Avancer"):
        #On vérifie si on peut (pas de future collision)
        if(not willCollideForward(ship,map)):
            #Dans ce cas on avance
            moveShipForward(ship,map)
            #Coûte un point d'action
            player.set_PA(player.PA - 1)
        else:
            print("Action impossible : collision")
    #Même chose   
    else:
        if(not willCollideBackward(ship,map)):
            moveShipBackward(ship,map)
            player.set_PA(player.PA - 1)
        else:
            print("Action impossible : collision")


def selectAction(map, player, player2):
    
    choice = input("Choisir une action : déplacer, pivoter, tirer, passer\n")
    match choice:
        case "déplacer":
            if(player.PA >= 1):
                moveShip(map, player)
        case "pivoter":
            if(player.PA >= 2):
                rotateShip(map,player)
        case "tirer":
            if(player.PA >= 2):
                w = selectWeapon(player)
                s = selectShip(map, player)
                way = selectWay()
                Shoot(s, w, way, map, player, player2)
                player.set_PA(player.PA - 2)
        case "passer":
            player.set_PA(0)
    

def loadGame():

    map = Map(41)
    map.createMap()
    map.initializeBase()
    map.initializeShips()

    p1,p2 = initializePlayer(map, "Lucas","Leo")
    p1.initializeWeapon()
    p2.initializeWeapon()
    
    return(map,p1,p2)


def initializePlayer(map, name1,name2):

    #Création des joueurs
    p1 = Player(name1)
    p2 = Player(name2)

    #Attribution de leurs bases
    p1.addBase(map.bases[0])
    p2.addBase(map.bases[1])

    #Attribution de leurs bateaux respectifs
    for i in range (4):
        p1.addShip(map.ships[i])
    for j in range (4,8):
        p2.addShip(map.ships[j])

    return (p1,p2)


def rotateShip(map, player):

    #Permet au joueur de selectionner le bateau qu'il veut jouer en fonction de son ID
    ship = selectShip(map, player)

    #Choix de la rotation par l'utilisateur (gauche ou droite)
    rotationChoice = input("g ou d ?\n")

    #Calcul de la futur orientation du bateau
    if(rotationChoice == "g"):
        nextShipDirection = rotateShipLeft(ship)
    else:
        nextShipDirection = rotateShipRight(ship)
    
    if(not willCollideRotation(ship,nextShipDirection,map)):

        eraseShip(ship,map.matrix)

        ship.direction = nextShipDirection
        placeShip(ship,map.matrix)

        player.set_PA(player.PA - 2)
    else:
        print("Collision détectée")
    
    

