from collide import *
from placement import *
from ClassMap import *
from ClassPlayer import *
from Classbase import *
from ClassShip import *
from gameAction import *


def findPlayer(s: Ship, p1: Player, p2: Player):
    if(s.id >= 5):
        return p2
    else:
        return p1

    # Fonction pour faire baisser les PV du bateau attaqué en fonction des degats de l'arme attaquante
    # Si le bateau a plus de PV, il est détruit et enlever des class Player
def Attacked(s: Ship, w:Weapon, m: Map, p1: Player, p2: Player):
    s.health -= w.damages
    if(s.health <= 0):
        p = findPlayer(s, p1, p2)
        eraseShip(s, m.matrix)
        p.removeShip(s)
        m.removeShipMap(s)
        s.health = 0

        


def coordShooting(s: Ship):
        coordX = 0
        coordY = 0
        match s.direction:
            case "N":
                coordX = s.row - (s.size-1)
                coordY = s.col
            case "E":
                coordX = s.row
                coordY = s.col + (s.size-1)
            case "S":
                coordX = s.row + (s.size-1)
                coordY = s.col
            case "W":
                coordX = s.row
                coordY = s.col - (s.size-1)
        return coordX, coordY
    
def find_ship_by_id(m: Map, id):
        for ship in m.ships:
            if ship.get_id() == id:
                return ship
        return None

def reconizeObject(m: map,coordX: int, coordY: int):
        Object = m.matrix[coordX][coordY]
        if(Object[0] != "B"):
            return find_ship_by_id(m, int(Object[0]))
        else: 
            return  None


    #FAIRE UNE FONCTION POUR RETROUVER UN BATEAU EN FONCTION DES COORDONNEES
def Shoot(s: Ship, w: Weapon, m: Map, p1: Player, p2: Player):
        
        #Coordonnée du front du bateau
        coordX = coordShooting(s)[0]
        coordY = coordShooting(s)[1]

        match s.direction:
            case "N":
                for i in range(w.range+1):
                    if(coordX - i >= 0):
                        if(m.matrix[coordX - (i+1)][coordY] != "* "):
                            ship = reconizeObject(m,coordX - (i+1), coordY)
                            if(ship != None):
                                print("TOUCHE! par le bateau n°", s.id)
                                Attacked(ship, w, m, p1, p2)
                                return ship
                        else:
                            if(m.matrix[coordX - (i)][coordY] == "* "):
                                m.matrix[coordX - (i)][coordY] = "M "
                            if(m.matrix[coordX - (i)][coordY] == "M "):
                                m.matrix[coordX - (i)][coordY] = "* "
                    else:
                        print("fin du tir")
                        break
            case "E":
                for i in range(w.range+1):
                    if(coordY + i+1 <= m.size-1):
                        if(m.matrix[coordX][coordY + (i+1)] != "* " and m.matrix[coordX][coordY + (i+1)] != "M "):
                            ship = reconizeObject(m, coordX, coordY + (i+1))
                            if(ship != None):
                                print(f"TOUCHE! par le bateau n°{s.id}")
                                Attacked(ship, w, m, p1, p2)
                                return ship
                        else:
                            if(m.matrix[coordX][coordY + (i)] == "* "):
                                m.matrix[coordX][coordY + (i)] = "M "
                            if(m.matrix[coordX][coordY + (i)] == "M "):
                                m.matrix[coordX][coordY + (i)] = "* "
                    else:
                        print("fin du tir")
                        break
            case "S":
                for i in range(w.range+1):
                    if(coordX + i+1 <= m.size-1):
                        if(m.matrix[coordX + (i+1)][coordY] != "* "):
                            ship = reconizeObject(m, coordX + (i+1), coordY)
                            if(ship != None):
                                print(f"TOUCHE! par le bateau n°{s.id}")
                                Attacked(ship, w, m, p1, p2)
                                return ship
                        else:
                            if(m.matrix[coordX + (i)][coordY] == "* "):
                                m.matrix[coordX + (i)][coordY] = "M "
                            if(m.matrix[coordX + (i)][coordY] == "M "):
                                m.matrix[coordX + (i)][coordY] = "* "
                    else:
                        print("fin du tir")
                        break
            case "W":
                for i in range(w.range+1):
                    if(coordY - i >= 0):
                        if(m.matrix[coordX][coordY - (i+1)] != "* "):
                            ship = reconizeObject(m, coordX, coordY - (i+1))
                            if(ship != None):
                                print(f"TOUCHE! par le bateau n°{s.id}")
                                Attacked(ship, w, m, p1, p2)
                                return ship
                        else:
                            if(m.matrix[coordX][coordY - (i)] == "* "):
                                m.matrix[coordX][coordY - (i)] = "M "
                            if(m.matrix[coordX][coordY - (i)] == "M "):
                                m.matrix[coordX][coordY - (i)] = "* "
                    else:
                        print("fin du tir")
                        break


def print_ships(player):
    for ship in player.ship:
        print("Bateau {} - Position : ({},{}), Orientation : {}, Taille : {}, PV : {}/{}".format(ship.get_id(), ship.row, ship.col, ship.direction, ship.size, ship.health, ship.maxhealth))

def print_ships_map(map):
    for ship in map.ships:
        print("Bateau {} - Position : ({},{}), Orientation : {}, Taille : {}, PV : {}/{}".format(ship.get_id(), ship.row, ship.col, ship.direction, ship.size, ship.health, ship.maxhealth))


