from collide import *
from placement import *
from ClassMap import *
from ClassPlayer import *
from Shooting import *

#Défini qui joue en fonction du nombre de tour
def whoPlays(turn,p1,p2):
    if(turn %2 == 0):
        return p1
    else:
        return p2
 

def loadGame(size):

    map = Map(size)
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

    
def checkWinByOponentShip(map, player):
    #Booléen à retourner
    win = True
    #On regarde tous les bateaux encore sur la carte
    for ship in map.ships:
        #S'il y en a ne serait ce qu'un seul qui ne fait pas partie des bateaux du joueur actuel, alors il n'a pas tout détruit
        # et par conséquent, pas gagné donc on set win à False
        if ship not in player.ship:
            print(str(ship.id) + "est encore en vie, donc pas gagné")
            win = False
            break
    return win
